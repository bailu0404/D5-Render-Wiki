"""
cn_official_scraper.py
----------------------
抓取 d5render.cn 官网核心页面（国内官网，WordPress + Elementor 格式）
输出到 raw/cn/official/

目标页面：
- d5render.cn/pricing  → pricing.md（定价方案）
- d5render.cn/download → download.md（下载/版本/系统要求）
- d5render.cn          → homepage.md（产品矩阵/行业解决方案）

注意：部分价格数字由 JS 渲染，静态抓取可能缺失；
脚本会在输出文件顶部写入提示，提醒手动核实价格数字。
每次版本发布或产品更新后重新运行此脚本即可。
"""

import os
import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

BASE_URL = "https://www.d5render.cn"
OUTPUT_DIR = "raw/cn/official"

HEADERS = {
    "User-Agent": "D5WikiCNOfficialScraper/1.0 (documentation archiver)",
    "Accept": "text/html",
}

PAGES = {
    "pricing.md": f"{BASE_URL}/pricing",
    "download.md": f"{BASE_URL}/download",
    "homepage.md": BASE_URL,
}


class OfficialConverter(MarkdownConverter):
    """处理 WordPress + Elementor 官网特有的 HTML 元素"""

    def convert_figure(self, el, text, **kwargs):
        img = el.find("img")
        if img:
            src = img.get("src", "")
            alt = img.get("alt", "")
            return f"\n![{alt}]({src})\n\n"
        return text

    def convert_svg(self, el, text, **kwargs):
        return ""

    def convert_iframe(self, el, text, **kwargs):
        src = el.get("src", "")
        if src:
            return f"\n[嵌入视频]({src})\n\n"
        return ""


def fetch_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            return resp
        except Exception as e:
            if attempt == retries - 1:
                print(f"  [失败] {url}: {e}")
                return None
            time.sleep(2)


def scrape_page(url, filename):
    """
    抓取单个官网页面，返回 Markdown 文本。
    针对不同页面采用不同的内容选择器策略。
    """
    resp = fetch_with_retry(url)
    if not resp:
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # 移除无用元素
    for tag in soup.select(
        "nav, footer, header, script, style, svg, "
        ".elementor-location-header, .elementor-location-footer, "
        ".post-navigation, .comments-area, .sidebar, .widget"
    ):
        tag.decompose()

    # 提取页面标题
    title_el = soup.find("h1") or soup.find("title")
    title = title_el.get_text(strip=True) if title_el else url

    # 找主内容区域（Elementor 优先）
    content = (
        soup.select_one(".elementor-section-wrap")
        or soup.select_one(".elementor-inner")
        or soup.select_one("main")
        or soup.select_one(".entry-content")
        or soup.select_one("article")
        or soup.find("body")
    )

    if not content:
        return None

    # 移除正文内重复的 h1
    for h1 in content.find_all("h1"):
        h1.decompose()

    # 绝对路径化
    for img in content.find_all("img", src=True):
        img["src"] = urljoin(url, img["src"])
    for a in content.find_all("a", href=True):
        if a["href"].startswith("/"):
            a["href"] = urljoin(BASE_URL, a["href"])

    # 转换 Markdown
    converter = OfficialConverter(heading_style="ATX")
    md = converter.convert_soup(content)

    # 清理
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    md = md.strip()

    if not md:
        return None

    # 定价页：加价格核实提示
    notice = ""
    if "pricing" in filename:
        notice = (
            "> **注意**：定价数字由页面 JavaScript 渲染，静态抓取可能不完整。\n"
            "> 请访问 https://www.d5render.cn/pricing 核实最新价格后手动补充。\n"
            "> 已知：社区版免费，专业版按月订阅，团队版需联系商务，学生版免费。\n\n"
        )

    return f"# {title}\n\n{notice}{md}\n"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename, url in PAGES.items():
        filepath = os.path.join(OUTPUT_DIR, filename)
        print(f"[抓取] {url}")
        content = scrape_page(url, filename)

        if content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  → 已保存: {filepath}")
        else:
            print(f"  → 抓取失败或内容为空，跳过")

        time.sleep(1)

    print(f"\n完成！文件保存在 {OUTPUT_DIR}/")
    print("\n后续步骤：")
    print("  1. 检查 pricing.md，手动补充 JS 渲染的价格数字")
    print("  2. 在仓库目录运行 claude，让 Claude 处理 raw/cn/official/ → wiki/cn/")


if __name__ == "__main__":
    main()

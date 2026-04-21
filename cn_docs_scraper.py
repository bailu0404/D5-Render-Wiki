"""
cn_docs_scraper.py
------------------
抓取 docs.d5render.cn（国内中文文档站）
输出到 Clippings/cn/manual/

注意：docs.d5render.cn 无 sitemap，首页为卡片式导航，
采用"首页提取链接 + 对每个页面再递归提取一层内链"策略。
"""

import os
import re
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

BASE_URL = "https://docs.d5render.cn"
OUTPUT_DIR = "Clippings/cn/manual"

HEADERS = {
    "User-Agent": "D5WikiCNDocsScraper/1.0 (documentation archiver)",
    "Accept": "text/html",
}


class DocsConverter(MarkdownConverter):
    """处理文档站特有的 HTML 元素（兼容新版 markdownify）"""

    def convert_div(self, el, text, **kwargs):
        classes = el.get("class", [])
        if "bg-warning" in classes:
            return f"\n> ⚠️ {text.strip()}\n\n"
        if "bg-info" in classes or "bg-note" in classes:
            return f"\n> ℹ️ {text.strip()}\n\n"
        if "bg-success" in classes:
            return f"\n> ✅ {text.strip()}\n\n"
        if "bg-danger" in classes:
            return f"\n> ❌ {text.strip()}\n\n"
        return text

    def convert_figure(self, el, text, **kwargs):
        img = el.find("img")
        if img:
            src = img.get("src", "")
            alt = img.get("alt", "")
            return f"\n![{alt}]({src})\n\n"
        return text

    def convert_svg(self, el, text, **kwargs):
        return ""


def is_docs_url(url):
    """判断是否是文档站内部页面链接"""
    parsed = urlparse(url)
    return parsed.netloc in ("docs.d5render.cn", "") and parsed.scheme in ("https", "http", "")


def extract_links_from_page(url):
    """抓取一个页面，返回其中所有文档站内部链接"""
    links = set()
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a["href"].split("#")[0]  # 去掉锚点
            if not href:
                continue
            if href.startswith("/"):
                full = BASE_URL + href
            elif href.startswith(BASE_URL):
                full = href
            else:
                continue
            # 排除首页和非内容页（如登录、搜索等）
            path = urlparse(full).path.strip("/")
            if path and not any(x in path for x in ["login", "search", "404"]):
                links.add(full)
    except Exception as e:
        print(f"  [提取链接失败] {url}: {e}")
    return links


def discover_all_urls():
    """两层链接发现：首页 → 所有内页 → 再从内页发现更多页面"""
    print(f"[发现] 抓取首页链接: {BASE_URL}")
    first_level = extract_links_from_page(BASE_URL)
    print(f"[发现] 首页找到 {len(first_level)} 个链接，开始第二层扫描...")

    all_urls = set(first_level)
    for i, url in enumerate(sorted(first_level), 1):
        print(f"  [扫描 {i}/{len(first_level)}] {url}")
        second_level = extract_links_from_page(url)
        new = second_level - all_urls
        if new:
            print(f"    → 发现 {len(new)} 个新链接")
        all_urls |= second_level
        time.sleep(0.3)

    print(f"[发现] 共找到 {len(all_urls)} 个文档页面\n")
    return sorted(all_urls)


def url_to_filename(url):
    """将 URL 路径转换为文件名，例如 /rendering/pbr → rendering -- pbr.md"""
    path = urlparse(url).path.strip("/")
    if not path:
        return "index.md"
    return path.replace("/", " -- ") + ".md"


def scrape_page(url):
    """抓取单个文档页面，返回 Markdown 文本"""
    for attempt in range(3):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            break
        except Exception as e:
            if attempt == 2:
                print(f"  [失败] {url}: {e}")
                return None
            time.sleep(2)

    soup = BeautifulSoup(resp.text, "html.parser")

    # 移除无用元素
    for tag in soup.select("nav, footer, script, style, svg, "
                           "[data-testid='feedback'], .hash-div"):
        tag.decompose()

    # 找主内容区域（按优先级依次尝试）
    main = (soup.select_one(".editor_js--markdown") or
            soup.select_one("main") or
            soup.find(attrs={"role": "main"}) or
            soup.find("article") or
            soup.body)

    if not main:
        return None

    # 提取标题
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else url.split("/")[-1]
    if h1:
        h1.decompose()

    # 将相对链接和图片转为绝对路径
    for img in main.find_all("img", src=True):
        img["src"] = urljoin(url, img["src"])
    for a in main.find_all("a", href=True):
        if a["href"].startswith("/"):
            a["href"] = urljoin(BASE_URL, a["href"])

    # 转换为 Markdown
    converter = DocsConverter(heading_style="ATX")
    md = converter.convert_soup(main)

    # 清理
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    md = re.sub(r"\[#\].*", "", md)
    md = re.sub(r"Last updated.*", "", md)
    md = re.sub(r"上次更新.*", "", md)
    md = re.sub(r"(Previous|Next|上一页|下一页)\n.*\n", "", md)
    md = md.strip()

    if not md:
        return None

    return f"# {title}\n\n{md}\n"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    urls = discover_all_urls()

    for i, url in enumerate(urls, 1):
        filename = url_to_filename(url)
        filepath = os.path.join(OUTPUT_DIR, filename)

        # 已存在且不为空则跳过（支持断点续抓）
        if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
            print(f"[{i}/{len(urls)}] 跳过（已存在）: {filename}")
            continue

        print(f"[{i}/{len(urls)}] 抓取: {url}")
        content = scrape_page(url)
        if content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  → 已保存: {filename}")
        else:
            print(f"  → 内容为空，跳过")

        time.sleep(0.5)

    print(f"\n完成！文件保存在 {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

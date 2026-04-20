"""
cn_news_scraper.py
------------------
抓取 d5render.cn/news（国内新闻，WordPress + Elementor 格式）
输出到 Clippings/cn/news/

注意：
- 新闻列表页无分页，所有文章在同一页（部分通过 JS 渲染）
- 已知文章 URL 作为兜底备用列表
- 正文在 .elementor-text-editor 容器内
"""

import os
import re
import time
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

BASE_URL = "https://www.d5render.cn"
NEWS_INDEX_URL = "https://www.d5render.cn/news"
OUTPUT_DIR = "Clippings/cn/news"

HEADERS = {
    "User-Agent": "D5WikiCNNewsScraper/1.0 (documentation archiver)",
    "Accept": "text/html",
}

# 兜底列表：静态 HTML 中 JS 渲染的文章可能抓不到，手动补充已知 URL
KNOWN_URLS = [
    "https://www.d5render.cn/news/d5-engine/",
    "https://www.d5render.cn/news/release-3-0/",
    "https://www.d5render.cn/news/2025-annual-review/",
    "https://www.d5render.cn/news/d5-become-universal-language/",
    "https://www.d5render.cn/news/lan-arc/",
    "https://www.d5render.cn/news/d5-seu-open-day/",
    "https://www.d5render.cn/news/2025-year-end/",
    "https://www.d5render.cn/news/design-industry-trend-2025/",
    "https://www.d5render.cn/news/blog-d5-team/",
    "https://www.d5render.cn/news/ai-report-2025/",
]


class NewsConverter(MarkdownConverter):
    """处理 WordPress + Elementor 特有的 HTML 元素（兼容新版 markdownify）"""

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
    """带重试的 HTTP 请求"""
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


def fetch_article_urls():
    """
    从 /news 列表页抓取文章 URL，合并兜底列表去重后返回。
    该页面无分页，所有文章在同一页（部分 JS 渲染）。
    """
    urls = set(KNOWN_URLS)  # 先放入已知 URL

    print(f"[列表页] 抓取: {NEWS_INDEX_URL}")
    resp = fetch_with_retry(NEWS_INDEX_URL)

    if resp:
        soup = BeautifulSoup(resp.text, "html.parser")
        # 尝试多种选择器
        links = soup.select(".entry-card .entry-title a, .entry-title a, article a[href*='/news/']")
        for a in links:
            href = a.get("href", "")
            # 过滤：必须含 /news/，且不含查询参数（?），且有实际 slug
            if "/news/" in href and "?" not in href:
                if not href.startswith("http"):
                    href = BASE_URL + href
                # 确保 /news/ 后面有 slug（不是纯列表页）
                slug = href.rstrip("/").split("/news/")[-1]
                if slug:
                    urls.add(href.rstrip("/") + "/")

        scraped = len(urls) - len(KNOWN_URLS)
        print(f"  → 页面抓取到 {max(scraped, 0)} 个额外链接")

    print(f"  → 合并后共 {len(urls)} 篇文章（含兜底列表）\n")
    return sorted(urls)


def scrape_article(url):
    """抓取单篇新闻文章，返回带 frontmatter 的 Markdown"""
    resp = fetch_with_retry(url)
    if not resp:
        return None

    soup = BeautifulSoup(resp.text, "html.parser")

    # 404 检测
    if soup.title and "404" in (soup.title.string or ""):
        return None

    # --- 提取元数据 ---

    # 标题
    title_el = soup.find("h1") or soup.select_one(".entry-title")
    title = title_el.get_text(strip=True) if title_el else url.rstrip("/").split("/")[-1]

    # 日期
    date = ""
    date_el = (soup.select_one("time[datetime]") or
               soup.select_one(".entry-date") or
               soup.select_one(".post-date"))
    if date_el:
        date = date_el.get("datetime", "") or date_el.get_text(strip=True)

    # 分类
    category = ""
    cat_el = (soup.select_one(".cat-links a") or
               soup.select_one(".entry-category a") or
               soup.select_one('[class*="category"] a'))
    if cat_el:
        category = cat_el.get_text(strip=True)

    # 作者
    author = ""
    author_el = (soup.select_one(".author-name") or
                 soup.select_one(".entry-author"))
    if author_el:
        author = author_el.get_text(strip=True)

    # --- 提取正文 ---

    # 移除无用区域
    for tag in soup.select("nav, footer, header, script, style, svg, "
                           ".post-navigation, .comments-area, .sidebar, "
                           ".widget, .related-posts, .elementor-location-header, "
                           ".elementor-location-footer"):
        tag.decompose()

    # 找正文容器（Elementor 优先，再降级到标准 WordPress）
    content = (soup.select_one(".elementor-text-editor") or
               soup.select_one('[data-prefix="news_single"] .elementor-container') or
               soup.select_one(".entry-content") or
               soup.select_one(".post-content") or
               soup.select_one("article") or
               soup.select_one("main"))

    if not content:
        return None

    # 移除正文内重复的 h1
    for h1 in content.find_all("h1"):
        h1.decompose()

    # 相对路径转绝对路径
    for img in content.find_all("img", src=True):
        img["src"] = urljoin(url, img["src"])
    for a in content.find_all("a", href=True):
        if a["href"].startswith("/"):
            a["href"] = urljoin(BASE_URL, a["href"])

    # 转换 Markdown
    converter = NewsConverter(heading_style="ATX")
    md = converter.convert_soup(content)

    # 清理
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    md = md.strip()

    if not md:
        return None

    frontmatter = f"""---
title: "{title}"
category: "{category}"
date: "{date}"
author: "{author}"
source: "{url}"
---"""

    return f"{frontmatter}\n\n# {title}\n\n{md}\n"


def url_to_filename(url):
    """将文章 URL 转为文件名：/news/d5-engine/ → d5-engine.md"""
    slug = url.rstrip("/").split("/")[-1]
    return slug + ".md"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    urls = fetch_article_urls()

    for i, url in enumerate(urls, 1):
        filename = url_to_filename(url)
        filepath = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(filepath) and os.path.getsize(filepath) > 100:
            print(f"[{i}/{len(urls)}] 跳过（已存在）: {filename}")
            continue

        print(f"[{i}/{len(urls)}] 抓取: {url}")
        content = scrape_article(url)

        if content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  → 已保存: {filename}")
        else:
            print(f"  → 抓取失败或内容为空，跳过")

        time.sleep(0.5)

    print(f"\n完成！文件保存在 {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

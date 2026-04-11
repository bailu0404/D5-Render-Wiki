#!/usr/bin/env python3
"""
D5 Render Blog Scraper
Crawls https://www.d5render.com/blog and saves all blog posts as Markdown files.
"""

import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter


# ── Configuration ──────────────────────────────────────────────────────────
BASE_URL = "https://www.d5render.com"
BLOG_LIST_URL = f"{BASE_URL}/blog"
OUTPUT_DIR = Path(__file__).parent / "Clippings" / "blog"
DELAY = 0.5
TIMEOUT = 30
MAX_RETRIES = 3


class BlogConverter(MarkdownConverter):
    """Custom converter for Webflow-based blog posts."""

    def convert_figure(self, el, text, parent_tags=None):
        img = el.find("img")
        if img:
            src = img.get("src", "")
            alt = img.get("alt", "")
            return f"\n![{alt}]({src})\n\n"
        return text

    def convert_svg(self, el, text, parent_tags=None):
        return ""

    def convert_iframe(self, el, text, parent_tags=None):
        src = el.get("src", "")
        if src:
            return f"\n[Embedded video]({src})\n\n"
        return ""


def blog_html_to_markdown(html: str, url: str) -> str:
    """Convert a D5 blog post page to Markdown."""
    soup = BeautifulSoup(html, "lxml")

    # Extract metadata
    title_el = soup.find("h1") or soup.find(attrs={"class": "post-title"})
    title = title_el.get_text(strip=True) if title_el else ""

    # Detect 404 pages
    if title == "404":
        return ""

    # Extract category tag (from blog-tag-button, not the "next articles" ones)
    tag = ""
    tag_buttons = soup.find_all("a", class_="blog-tag-button")
    for btn in tag_buttons:
        text = btn.get_text(strip=True)
        if text and not re.match(r"[A-Z][a-z]+ \d{1,2}, \d{4}", text):
            tag = text
            break

    # Extract date (from blog-tag-button that looks like a date)
    date = ""
    for btn in tag_buttons:
        text = btn.get_text(strip=True)
        date_match = re.match(r"([A-Z][a-z]+ \d{1,2}, \d{4})", text)
        if date_match:
            date = date_match.group(1)
            break

    # Find author name
    author_name_el = soup.find(attrs={"class": "author-name-text"})
    author = author_name_el.get_text(strip=True) if author_name_el else ""

    # Find main content area (Webflow rich text)
    content = soup.find("main", class_="post-content")
    if not content:
        content = soup.find("div", class_="w-richtext")
    if not content:
        return ""

    # Remove unwanted elements
    for sel in ["nav", "svg", "script", "style"]:
        for el in content.select(sel):
            el.decompose()

    # Remove "You might also like" section and share buttons
    for el in soup.find_all(attrs={"class": lambda c: c and any(
        kw in " ".join(c) if isinstance(c, list) else ""
        for kw in ["blog-post-next", "post-social", "share"]
    )}):
        el.decompose()

    # Make image URLs absolute
    for img in content.find_all("img"):
        src = img.get("src", "")
        if src and not src.startswith(("http://", "https://", "data:")):
            img["src"] = urljoin(url, src)

    # Make links absolute
    for a in content.find_all("a"):
        href = a.get("href", "")
        if href.startswith("/"):
            a["href"] = urljoin(BASE_URL, href)

    # Convert to markdown
    converter = BlogConverter(
        heading_style="atx",
        bullets="-",
        strong_em_symbol="**",
        strip=["script", "style"],
    )
    md = converter.convert_soup(content)

    # ── Post-processing ─────────────────────────────────────────────────
    md = re.sub(r"\n{4,}", "\n\n\n", md)

    # Remove leftover navigation/share artifacts
    md = re.sub(r"Share\s*$", "", md, flags=re.MULTILINE)
    md = re.sub(r"You might also like.*", "", md, flags=re.DOTALL)

    # Clean up Webflow artifacts
    md = re.sub(r"‹\s*Back to Blog\s*›?", "", md)

    md = md.strip()

    # Build frontmatter + title
    frontmatter = "---\n"
    if title:
        frontmatter += f"title: \"{title.replace('\"', '\\\"')}\"\n"
    if tag:
        frontmatter += f"category: \"{tag}\"\n"
    if date:
        frontmatter += f"date: \"{date}\"\n"
    if author:
        frontmatter += f"author: \"{author}\"\n"
    frontmatter += f"source: \"{url}\"\n"
    frontmatter += "---\n\n"

    if title:
        md = frontmatter + f"# {title}\n\n" + md
    else:
        md = frontmatter + md

    return md


def discover_blog_posts(session: requests.Session) -> list[str]:
    """Discover all blog post URLs from the blog listing page."""
    print(f"Fetching blog listing: {BLOG_LIST_URL}")
    resp = session.get(BLOG_LIST_URL, timeout=TIMEOUT)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")

    post_urls = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("/posts/"):
            full_url = urljoin(BASE_URL, href)
            post_urls.add(full_url)

    print(f"Found {len(post_urls)} blog posts on listing page")
    return sorted(post_urls)


def fetch_page(url: str, session: requests.Session) -> str | None:
    """Fetch a page with retry logic."""
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.get(url, timeout=TIMEOUT)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            print(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(2)
    return None


def url_to_filepath(url: str) -> Path:
    """Convert a blog post URL to a file path."""
    # Extract the slug from /posts/slug-name
    slug = url.rstrip("/").split("/posts/")[-1]
    return OUTPUT_DIR / f"{slug}.md"


def main():
    print("=" * 60)
    print("D5 Render Blog Scraper")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

    session = requests.Session()
    session.headers.update({
        "User-Agent": "D5BlogScraper/1.0 (documentation archiver)",
        "Accept": "text/html",
    })

    # Step 1: Discover all blog posts
    urls = discover_blog_posts(session)

    if not urls:
        print("No blog posts found!")
        return

    print(f"\nWill scrape {len(urls)} blog posts")

    # Step 2: Scrape each post
    success = 0
    failed = 0
    skipped = 0

    for i, url in enumerate(urls, 1):
        filepath = url_to_filepath(url)
        rel_path = filepath.relative_to(OUTPUT_DIR)

        # Resume support
        if filepath.exists() and filepath.stat().st_size > 100:
            skipped += 1
            print(f"[{i}/{len(urls)}] SKIP (exists): {rel_path}")
            continue

        slug = url.split("/posts/")[-1]
        print(f"[{i}/{len(urls)}] Fetching: {slug}")

        html = fetch_page(url, session)
        if not html:
            failed += 1
            print(f"  FAILED: {url}")
            continue

        md = blog_html_to_markdown(html, url)
        if not md or len(md.strip()) < 50:
            skipped += 1
            print(f"  SKIP: Empty or minimal content ({len(md)} chars)")
            continue

        filepath.write_text(md, encoding="utf-8")
        size_kb = filepath.stat().st_size / 1024
        print(f"  Saved: {rel_path} ({size_kb:.1f} KB)")
        success += 1

        time.sleep(DELAY)

    # Summary
    print("\n" + "=" * 60)
    print(f"Done! Scraped: {success}, Skipped: {skipped}, Failed: {failed}")
    print(f"Total posts: {len(urls)}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()

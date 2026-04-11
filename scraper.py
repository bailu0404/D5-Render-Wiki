#!/usr/bin/env python3
"""
D5 Render Docs Scraper
Crawls https://docs.d5render.com/ and saves all pages as Markdown files.
"""

import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

# ── Configuration ──────────────────────────────────────────────────────────
BASE_URL = "https://docs.d5render.com"
SITEMAP_URL = f"{BASE_URL}/sitemap-pages.xml"
OUTPUT_DIR = Path(__file__).parent / "Clippings"
DELAY = 0.5  # seconds between requests (be polite)
TIMEOUT = 30
MAX_RETRIES = 3

# ── GitBook-aware Markdown converter ───────────────────────────────────────
class GitBookConverter(MarkdownConverter):
    """Custom converter that handles GitBook-specific HTML structures."""

    def convert_hint(self, el, text, parent_tags=None):
        # GitBook hint/callout boxes
        classes = " ".join(el.get("class", []))
        if "bg-warning" in classes:
            return f"\n> ⚠️ {text.strip()}\n\n"
        elif "bg-info" in classes or "bg-note" in classes:
            return f"\n> ℹ️ {text.strip()}\n\n"
        elif "bg-success" in classes:
            return f"\n> ✅ {text.strip()}\n\n"
        elif "bg-danger" in classes:
            return f"\n> ❌ {text.strip()}\n\n"
        return f"\n> {text.strip()}\n\n"

    def convert_div(self, el, text, parent_tags=None):
        classes = " ".join(el.get("class", []))
        # Skip empty divs or purely structural ones
        if not text.strip():
            return ""
        # Handle hint/callout boxes
        if "hint" in classes:
            return self.convert_hint(el, text, parent_tags=parent_tags)
        # Skip wrapper divs that just contain other converted content
        return text

    def convert_figure(self, el, text, parent_tags=None):
        # Extract image from figure
        img = el.find("img")
        if img:
            src = img.get("src", "")
            alt = img.get("alt", "")
            return f"\n![{alt}]({src})\n\n"
        return text

    def convert_svg(self, el, text, parent_tags=None):
        # Skip SVG icons (hash links, chevrons, etc.)
        return ""


def html_to_markdown(html: str, url: str) -> str:
    """Convert a GitBook page's HTML to clean Markdown."""
    soup = BeautifulSoup(html, "lxml")

    # Extract title from <h1>
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else ""

    # Find main content area
    main = soup.find("main")
    if not main:
        return ""

    # Remove elements we don't want in the output
    for sel in [
        # Breadcrumbs
        "ol",  # breadcrumb navigation
        # Hash/anchor links in headings
        "div.hash",
        "div[class*='hash']",
        # Navigation helpers
        "nav",
        # SVG icons
        "svg",
        # Header with emoji breadcrumb
        "header",
        # "Was this helpful?" footer
        "div[class*='feedback']",
    ]:
        for el in main.select(sel):
            el.decompose()

    # Also remove the h1 from content since we'll add it as frontmatter title
    if h1 and h1.parent == main:
        h1.decompose()
    elif h1:
        # Find and remove h1 in the main content
        for h in main.find_all("h1"):
            h.decompose()
            break

    # Convert image src to absolute URLs
    for img in main.find_all("img"):
        src = img.get("src", "")
        if src and not src.startswith(("http://", "https://", "data:")):
            img["src"] = urljoin(url, src)

    # Convert links to absolute URLs or internal wiki links
    for a in main.find_all("a"):
        href = a.get("href", "")
        if href.startswith("/"):
            a["href"] = urljoin(BASE_URL, href)

    # Convert to markdown
    converter = GitBookConverter(
        heading_style="atx",
        bullets="-",
        strong_em_symbol="**",
        strip=["script", "style"],
    )
    md = converter.convert_soup(main)

    # ── Post-processing cleanup ────────────────────────────────────────────
    # Remove excessive blank lines
    md = re.sub(r"\n{4,}", "\n\n\n", md)

    # Clean up hash anchor artifacts
    md = re.sub(r"\[#\]\([^)]*\)", "", md)
    md = re.sub(r"hashtag", "", md)

    # Clean up remaining emoji artifacts from navigation
    md = re.sub(r"chevron-right", "", md)
    md = re.sub(r"chevron-down", "", md)

    # Clean up broken list items (GitBook sometimes has empty <li>)
    md = re.sub(r"^- \s*\n", "", md, flags=re.MULTILINE)

    # Remove "Last updated X ago" footer lines
    md = re.sub(r"\n*Last updated\s+.*(?:ago|\d{4})\s*\n*", "\n", md)

    # Remove Previous/Next navigation links at the bottom of pages
    md = re.sub(r"\n*\[Previous[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"\n*\[Next[^\]]*\]\([^)]*\)", "", md)

    # Remove "circle-exclamation" or similar icon artifacts
    md = re.sub(r"\bcircle-exclamation\b", "", md)

    # Remove leading/trailing whitespace
    md = md.strip()

    # Add title at top
    if title:
        md = f"# {title}\n\n{md}"

    return md


def url_to_filepath(url: str) -> Path:
    """Convert a URL to a file path for saving."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    if not path:
        return OUTPUT_DIR / "index.md"

    # Replace slashes with a separator that preserves hierarchy in the filename
    # Use " -- " as section separator in filename
    filename = path.replace("/", " -- ") + ".md"
    return OUTPUT_DIR / filename


def fetch_sitemap_urls() -> list[str]:
    """Fetch and parse the sitemap to get all page URLs."""
    print(f"Fetching sitemap: {SITEMAP_URL}")
    resp = requests.get(SITEMAP_URL, timeout=TIMEOUT)
    resp.raise_for_status()

    root = ET.fromstring(resp.text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    urls = []
    for loc in root.findall(".//sm:loc", ns):
        url = loc.text.strip()
        if url.startswith(BASE_URL):
            urls.append(url)

    # Deduplicate and sort
    urls = sorted(set(urls))
    return urls


def fetch_page(url: str, session: requests.Session) -> str | None:
    """Fetch a single page with retry logic."""
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.get(url, timeout=TIMEOUT)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            print(f"  Attempt {attempt + 1}/{MAX_RETRIES} failed for {url}: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(2)
    return None


def main():
    print("=" * 60)
    print("D5 Render Docs Scraper")
    print("=" * 60)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

    # Step 1: Get all URLs from sitemap
    urls = fetch_sitemap_urls()
    print(f"Found {len(urls)} pages in sitemap")

    # Step 2: Also scrape the sidebar navigation from the homepage to get the
    # full hierarchy (some pages might not be in the sitemap)
    print("\nFetching sidebar navigation from homepage...")
    session = requests.Session()
    session.headers.update({
        "User-Agent": "D5WikiScraper/1.0 (documentation archiver)",
        "Accept": "text/html",
    })

    homepage = fetch_page(BASE_URL, session)
    if homepage:
        soup = BeautifulSoup(homepage, "lxml")
        sidebar = soup.find(attrs={"data-testid": "table-of-contents"})
        if sidebar:
            for a in sidebar.find_all("a", href=True):
                full_url = urljoin(BASE_URL, a["href"])
                if full_url.startswith(BASE_URL) and full_url not in urls:
                    urls.append(full_url)
            print(f"After sidebar scan: {len(urls)} total URLs")

    # Deduplicate
    urls = sorted(set(urls))
    print(f"\nWill scrape {len(urls)} unique pages")

    # Step 3: Scrape each page
    success = 0
    failed = 0
    skipped = 0

    for i, url in enumerate(urls, 1):
        filepath = url_to_filepath(url)
        rel_path = filepath.relative_to(OUTPUT_DIR)

        # Skip if already downloaded (resume support)
        if filepath.exists() and filepath.stat().st_size > 100:
            skipped += 1
            print(f"[{i}/{len(urls)}] SKIP (exists): {rel_path}")
            continue

        path_display = url.replace(BASE_URL, "") or "/"
        print(f"[{i}/{len(urls)}] Fetching: {path_display}")

        html = fetch_page(url, session)
        if not html:
            failed += 1
            print(f"  FAILED: Could not fetch {url}")
            continue

        # Convert to markdown
        md = html_to_markdown(html, url)
        if not md or len(md.strip()) < 20:
            # Some pages are just section headers with no content
            skipped += 1
            print(f"  SKIP: Empty or minimal content ({len(md)} chars)")
            continue

        # Save
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(md, encoding="utf-8")
        size_kb = filepath.stat().st_size / 1024
        print(f"  Saved: {rel_path} ({size_kb:.1f} KB)")
        success += 1

        # Rate limiting
        time.sleep(DELAY)

    # Summary
    print("\n" + "=" * 60)
    print(f"Done! Scraped: {success}, Skipped: {skipped}, Failed: {failed}")
    print(f"Total pages: {len(urls)}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()

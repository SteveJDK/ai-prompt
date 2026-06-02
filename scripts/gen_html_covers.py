#!/usr/bin/env python3
"""
HTML Cover Generator for Pistack (Hugo)
Scans posts without covers, generates an HTML cover based on title/tags,
takes a screenshot, and updates the frontmatter.
"""

import os
import re
import sys
import asyncio
import frontmatter
from playwright.async_api import async_playwright

# Configuration
SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(SITE_ROOT, "content/posts")
STATIC_DIR = os.path.join(SITE_ROOT, "static/img/covers")

os.makedirs(STATIC_DIR, exist_ok=True)

# HTML Templates based on tags/content type
TEMPLATES = {
    "default": """
    <div style="height:100vh; width:100vw; display:flex; flex-direction:column; justify-content:center; align-items:center; background:linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); color:white; font-family:sans-serif; padding:40px; box-sizing:border-box; text-align:center;">
        <div style="font-size:80px; margin-bottom:20px;">🚀</div>
        <h1 style="font-size:48px; font-weight:800; margin:0; text-transform:uppercase; letter-spacing:2px;">{title}</h1>
        <p style="font-size:24px; color:#a0a0a0; margin-top:20px; max-width:80%;">{subtitle}</p>
    </div>
    """,
    "code": """
    <div style="height:100vh; width:100vw; display:flex; flex-direction:column; justify-content:center; align-items:center; background:#0d1117; color:#58a6ff; font-family:monospace; padding:40px; box-sizing:border-box;">
        <div style="border:1px solid #30363d; border-radius:8px; padding:20px; background:#161b22; width:80%; box-shadow:0 0 20px rgba(88,166,255,0.2);">
            <div style="color:#7ee787; margin-bottom:10px;">$ {title}</div>
            <div style="color:#c9d1d9;">Generating awesome content...</div>
            <div style="color:#c9d1d9;">Done. ✅</div>
        </div>
        <h1 style="font-size:42px; margin-top:30px; color:white;">{title}</h1>
    </div>
    """
}

async def screenshot_html(html_content, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1200, "height": 630}) # OG Image size
        await page.set_content(html_content, wait_until="networkidle")
        await page.wait_for_timeout(500)
        await page.screenshot(path=output_path, full_page=False)
        await browser.close()
    return output_path

def process_post(filepath):
    with open(filepath, 'r') as f:
        post = frontmatter.load(f)
        
    if 'cover' in post.metadata and post.metadata['cover']:
        print(f"Skipping {filepath}: already has cover")
        return

    title = post.metadata.get('title', 'Untitled')
    tags = post.metadata.get('tags', [])
    tags_str = [str(t).lower() for t in tags]
    
    # Select template
    template = TEMPLATES.get('default')
    if any(t in tags_str for t in ['code', 'dev', 'programming', 'linux']):
        template = TEMPLATES.get('code')
        
    # Fill template
    html = template.format(title=title, subtitle=post.metadata.get('description', ''))
    
    # Generate filename
    slug = post.metadata.get('slug', os.path.splitext(os.path.basename(filepath))[0])
    img_filename = f"{slug}.png"
    img_path = os.path.join(STATIC_DIR, img_filename)
    
    # Run screenshot
    print(f"Generating cover for {title}...")
    asyncio.run(screenshot_html(html, img_path))
    
    # Update frontmatter
    post.metadata['cover'] = f"/img/covers/{img_filename}"
    
    with open(filepath, 'wb') as f:
        frontmatter.dump(post, f)
    print(f"Updated {filepath} with cover {img_filename}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_post(sys.argv[1])
    else:
        for root, _, files in os.walk(CONTENT_DIR):
            for f in files:
                if f.endswith('.md'):
                    process_post(os.path.join(root, f))
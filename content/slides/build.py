"""
build.py — Render HTML slides to PDF and merge into final deck.

Requirements:
    pip install playwright
    playwright install chromium

Usage:
    cd content/slides
    python build.py

Output:
    agentic-sdlc-hackathon-slides.pdf
"""

import base64
import glob
import os
import re
import subprocess
import sys

LOGO_DARK = os.path.join(os.path.dirname(__file__), "ey-logo-dark.png")
OUTPUT_PDF = os.path.join(os.path.dirname(__file__), "agentic-sdlc-hackathon-slides.pdf")


def embed_logo(html: str) -> str:
    """Replace ey-logo-dark.png src with inline base64 so Playwright renders it."""
    with open(LOGO_DARK, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    data_uri = f"data:image/png;base64,{b64}"
    return re.sub(r'src=["\'](?:\.\/)?ey-logo-dark\.png["\']', f'src="{data_uri}"', html)


def render_slides():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("playwright not installed — run: pip install playwright && playwright install chromium")

    slide_files = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "slide-*.html")))
    if not slide_files:
        sys.exit("No slide-*.html files found in this directory.")

    print(f"Found {len(slide_files)} slides.")
    pdf_files = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for html_file in slide_files:
            pdf_file = html_file.replace(".html", ".pdf")
            pdf_files.append(pdf_file)

            with open(html_file, "r", encoding="utf-8") as f:
                html = embed_logo(f.read())

            temp_file = html_file.replace(".html", "_tmp.html")
            with open(temp_file, "w", encoding="utf-8") as f:
                f.write(html)

            page.goto(f"file:///{os.path.abspath(temp_file).replace(os.sep, '/')}")
            page.pdf(
                path=pdf_file,
                width="1920px",
                height="1080px",
                print_background=True,
                scale=1,
            )
            os.remove(temp_file)
            print(f"  {os.path.basename(html_file)} -> {os.path.basename(pdf_file)}")

        browser.close()

    return pdf_files


def merge_pdfs(pdf_files: list[str]):
    """Merge individual PDFs using pdfunite (Linux/macOS) or PyPDF2 fallback."""
    # Try pdfunite first
    try:
        subprocess.run(
            ["pdfunite"] + pdf_files + [OUTPUT_PDF],
            check=True,
            capture_output=True,
        )
        print(f"\nMerged with pdfunite -> {os.path.basename(OUTPUT_PDF)}")
        return
    except (FileNotFoundError, subprocess.CalledProcessError):
        pass

    # Fallback: PyPDF2
    try:
        from PyPDF2 import PdfMerger
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)
        merger.write(OUTPUT_PDF)
        merger.close()
        print(f"\nMerged with PyPDF2 -> {os.path.basename(OUTPUT_PDF)}")
        return
    except ImportError:
        pass

    print("\npdfunite not found and PyPDF2 not installed.")
    print("To install PyPDF2: pip install PyPDF2")
    print("Individual PDFs are in content/slides/ — merge manually or install one of the above.")


if __name__ == "__main__":
    pdf_files = render_slides()
    if len(pdf_files) > 1:
        merge_pdfs(pdf_files)
    elif pdf_files:
        os.rename(pdf_files[0], OUTPUT_PDF)

    print(f"\nDone. Output: {OUTPUT_PDF}")

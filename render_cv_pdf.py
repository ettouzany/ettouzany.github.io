"""Render cv/cv-<lang>.html to A4 PDF with headless Chromium (Playwright).

    python3 gen_cv.py && python3 render_cv_pdf.py
"""

import os

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
CV_DIR = os.path.join(ROOT, "cv")
LANGS = ["en", "fr", "ar"]


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for code in LANGS:
            src = os.path.join(CV_DIR, "cv-%s.html" % code)
            out = os.path.join(CV_DIR, "noureddine-ettouzany-cv-%s.pdf" % code)
            page.goto("file://" + src, wait_until="networkidle")
            page.emulate_media(media="print")
            # fonts must be resolved before layout is frozen into the PDF
            page.evaluate("() => document.fonts.ready")
            page.pdf(path=out, format="A4", print_background=True,
                     margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                     prefer_css_page_size=True)
            print("wrote", out)
        browser.close()


if __name__ == "__main__":
    main()

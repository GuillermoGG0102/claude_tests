#!/usr/bin/env python3
"""
Convert HTML infographic to PNG screenshot.
Captures the HTML exactly as it renders.
"""

import subprocess
import sys
import os

def html_to_png(html_file, output_png):
    """
    Convert HTML file to PNG using WeasyPrint.
    """
    try:
        from weasyprint import HTML, CSS
    except ImportError:
        print("Installing weasyprint...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "weasyprint", "-q"])
        from weasyprint import HTML, CSS

    print(f"📸 Converting {html_file} to PNG...")

    # Get absolute path
    html_path = os.path.abspath(html_file)
    output_path = os.path.abspath(output_png)

    # First create PDF
    pdf_path = output_path.replace('.png', '.pdf')
    HTML(filename=html_path).write_pdf(pdf_path)

    # Then convert PDF to PNG using pdf2image
    try:
        from pdf2image import convert_from_path
    except ImportError:
        print("Installing pdf2image...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pdf2image", "-q"])
        from pdf2image import convert_from_path

    print("Converting PDF to PNG...")
    images = convert_from_path(pdf_path, dpi=150)

    if images:
        # Save first (and only) image
        images[0].save(output_path, 'PNG')
        # Clean up PDF
        os.remove(pdf_path)

    print(f"✅ PNG created: {output_path}")
    print(f"📊 Perfect for LinkedIn sharing!")

if __name__ == "__main__":
    html_file = "examples/claude-skills-linkedin.html"
    output_png = "examples/claude-skills-infographic.png"

    html_to_png(html_file, output_png)

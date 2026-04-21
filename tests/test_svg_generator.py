#!/usr/bin/env python3
"""
Test suite for SVG generator utility.

Tests cover:
- File creation and saving
- SVG validation
- Error handling
- Path operations
- Content handling
"""

import os
import tempfile
from pathlib import Path
import pytest
import sys

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from svg_generator import save_svg, validate_svg


class TestSVGValidation:
    """Test SVG structure validation."""

    def test_valid_basic_svg(self):
        """Test validation of basic SVG structure."""
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><circle/></svg>'
        is_valid, message = validate_svg(svg)
        assert is_valid

    def test_valid_svg_with_dimensions(self):
        """Test SVG with width and height."""
        svg = '<svg width="100" height="100"><rect/></svg>'
        is_valid, message = validate_svg(svg)
        assert is_valid

    def test_valid_svg_with_viewbox(self):
        """Test SVG with viewBox."""
        svg = '<svg viewBox="0 0 100 100"><rect/></svg>'
        is_valid, message = validate_svg(svg)
        assert is_valid

    def test_missing_opening_tag(self):
        """Test SVG without opening tag."""
        svg = '<circle/></svg>'
        is_valid, message = validate_svg(svg)
        assert not is_valid
        assert "svg" in message.lower()

    def test_missing_closing_tag(self):
        """Test SVG without closing tag."""
        svg = '<svg><circle/>'
        is_valid, message = validate_svg(svg)
        assert not is_valid
        assert "</svg>" in message.lower()

    def test_empty_svg(self):
        """Test empty SVG content."""
        svg = ''
        is_valid, message = validate_svg(svg)
        assert not is_valid

    def test_svg_case_insensitive(self):
        """Test that SVG validation is case-insensitive."""
        svg = '<SVG xmlns="http://www.w3.org/2000/svg"><rect/></SVG>'
        is_valid, message = validate_svg(svg)
        assert is_valid

    def test_svg_with_whitespace(self):
        """Test SVG with leading/trailing whitespace."""
        svg = '  \n<svg><rect/></svg>\n  '
        is_valid, message = validate_svg(svg)
        assert is_valid

    def test_missing_dimensions_warning(self):
        """Test that SVG without dimensions shows warning."""
        svg = '<svg><rect/></svg>'
        is_valid, message = validate_svg(svg)
        assert is_valid  # Still valid but with warning
        assert "warning" in message.lower() or "should have" in message.lower()


class TestSVGFileSaving:
    """Test SVG file saving functionality."""

    def test_save_svg_to_file(self):
        """Test saving SVG to a file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.svg")
            svg_content = '<svg><rect/></svg>'

            success = save_svg(filepath, svg_content)

            assert success
            assert os.path.exists(filepath)
            with open(filepath, 'r') as f:
                saved_content = f.read()
            assert saved_content == svg_content

    def test_save_svg_creates_directory(self):
        """Test that save_svg creates parent directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            nested_path = os.path.join(tmpdir, "nested", "dir", "test.svg")
            svg_content = '<svg><rect/></svg>'

            success = save_svg(nested_path, svg_content)

            assert success
            assert os.path.exists(nested_path)

    def test_save_svg_empty_content(self):
        """Test saving empty SVG content."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.svg")

            success = save_svg(filepath, '')

            assert not success

    def test_save_svg_whitespace_only(self):
        """Test saving whitespace-only content."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.svg")

            success = save_svg(filepath, '   \n  \t  ')

            assert not success

    def test_save_svg_with_validation(self):
        """Test saving with validation enabled."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.svg")
            svg_content = '<svg viewBox="0 0 100 100"><rect/></svg>'

            success = save_svg(filepath, svg_content, validate=True)

            assert success
            assert os.path.exists(filepath)

    def test_save_svg_invalid_with_validation(self):
        """Test saving invalid SVG with validation fails."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.svg")
            svg_content = '<invalid></svg>'

            success = save_svg(filepath, svg_content, validate=True)

            assert not success

    def test_save_svg_with_special_characters(self):
        """Test saving SVG with special characters."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.svg")
            svg_content = '<svg><text>Hello © 2024 & more</text></svg>'

            success = save_svg(filepath, svg_content)

            assert success
            with open(filepath, 'r', encoding='utf-8') as f:
                saved_content = f.read()
            assert '©' in saved_content
            assert '&' in saved_content

    def test_save_svg_utf8_encoding(self):
        """Test that SVG is saved with UTF-8 encoding."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "test.svg")
            svg_content = '<svg><text>Привет мир</text></svg>'

            success = save_svg(filepath, svg_content)

            assert success
            with open(filepath, 'r', encoding='utf-8') as f:
                saved_content = f.read()
            assert 'Привет' in saved_content


class TestSVGContent:
    """Test SVG content handling."""

    def test_complex_svg(self):
        """Test saving complex SVG with multiple elements."""
        svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="50" fill="blue"/>
            <rect x="50" y="50" width="100" height="100" fill="red" opacity="0.5"/>
            <text x="100" y="100" text-anchor="middle">Hello</text>
        </svg>'''

        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "complex.svg")
            success = save_svg(filepath, svg_content)

            assert success
            assert os.path.getsize(filepath) > 0

    def test_svg_with_style_tag(self):
        """Test SVG with style definitions."""
        svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
            <defs>
                <style>
                    .myclass { fill: red; stroke: blue; }
                </style>
            </defs>
            <circle class="myclass" cx="50" cy="50" r="40"/>
        </svg>'''

        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "styled.svg")
            success = save_svg(filepath, svg_content)

            assert success

    def test_svg_with_namespace(self):
        """Test SVG with proper namespace."""
        svg_content = '<svg xmlns="http://www.w3.org/2000/svg"><circle/></svg>'

        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "ns.svg")
            success = save_svg(filepath, svg_content)

            assert success


class TestPathHandling:
    """Test file path handling."""

    def test_save_with_relative_path(self):
        """Test saving with relative path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            old_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                success = save_svg("test.svg", '<svg><rect/></svg>')
                assert success
                assert os.path.exists("test.svg")
            finally:
                os.chdir(old_cwd)

    def test_save_with_absolute_path(self):
        """Test saving with absolute path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.abspath(os.path.join(tmpdir, "test.svg"))
            success = save_svg(filepath, '<svg><rect/></svg>')

            assert success
            assert os.path.exists(filepath)

    def test_filename_with_spaces(self):
        """Test saving file with spaces in name."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "my infographic file.svg")
            success = save_svg(filepath, '<svg><rect/></svg>')

            assert success
            assert os.path.exists(filepath)

    def test_filename_with_special_chars(self):
        """Test saving file with special characters in name."""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, "infographic-2024_v1.svg")
            success = save_svg(filepath, '<svg><rect/></svg>')

            assert success
            assert os.path.exists(filepath)


# Run tests if executed directly
if __name__ == '__main__':
    pytest.main([__file__, '-v'])

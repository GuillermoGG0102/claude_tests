#!/usr/bin/env python3
"""
SVG Generator - Save and manage SVG infographics

This utility script:
- Reads SVG code (from stdin or file)
- Validates basic SVG structure
- Saves to file with proper formatting
- Provides helpful feedback

Usage:
    # From stdin
    echo '<svg>...</svg>' | python svg_generator.py output.svg

    # From file
    python svg_generator.py output.svg < input.txt

    # With validation
    python svg_generator.py output.svg --validate

    # Help
    python svg_generator.py --help
"""

import argparse
import sys
from pathlib import Path
from typing import Optional


def validate_svg(content: str) -> tuple[bool, str]:
    """Validate basic SVG structure.

    Args:
        content: SVG code to validate

    Returns:
        Tuple of (is_valid, message)
    """
    content = content.strip()

    # Check for SVG opening tag
    if not content.lower().startswith('<svg'):
        return False, "SVG must start with <svg tag"

    # Check for SVG closing tag
    if not content.lower().endswith('</svg>'):
        return False, "SVG must end with </svg>"

    # Check for basic structure
    if '<svg' not in content.lower():
        return False, "Missing <svg opening tag"

    # Check if it has width/height or viewBox
    has_dimensions = (
        'width=' in content or
        'height=' in content or
        'viewBox=' in content
    )
    if not has_dimensions:
        return (True,
                "Warning: SVG should have width/height or viewBox attribute")

    return True, "SVG structure is valid"


def save_svg(filename: str, content: str, validate: bool = False) -> bool:
    """Save SVG content to file.

    Args:
        filename: Output file path
        content: SVG code to save
        validate: Whether to validate SVG before saving

    Returns:
        True if successful, False otherwise
    """
    content = content.strip()

    if not content:
        print("❌ Error: SVG content is empty", file=sys.stderr)
        return False

    # Validate if requested
    if validate:
        is_valid, message = validate_svg(content)
        print(f"📋 Validation: {message}")
        if not is_valid:
            print("❌ Error: SVG validation failed", file=sys.stderr)
            return False

    try:
        # Create parent directories if needed
        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)

        # Write SVG file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        # Get file size
        file_size = path.stat().st_size
        size_kb = file_size / 1024

        print(f"✅ SVG saved successfully!")
        print(f"   📁 File: {path.absolute()}")
        print(f"   📊 Size: {size_kb:.2f} KB ({file_size} bytes)")
        print(f"   🌐 Open in browser: file://{path.absolute()}")

        return True

    except IOError as e:
        print(f"❌ Error writing file: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Save SVG infographic code to files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  echo '<svg>...</svg>' | python svg_generator.py output.svg
  python svg_generator.py output.svg --validate < code.txt
  python svg_generator.py output.svg --validate
        """
    )

    parser.add_argument(
        'filename',
        help='Output SVG file path'
    )
    parser.add_argument(
        '--validate', '-v',
        action='store_true',
        help='Validate SVG structure before saving'
    )
    parser.add_argument(
        '--input', '-i',
        type=argparse.FileType('r'),
        default=sys.stdin,
        help='Input file (default: stdin)'
    )

    args = parser.parse_args()

    # Read SVG content
    try:
        svg_content = args.input.read()
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"❌ Error reading input: {e}", file=sys.stderr)
        return 1

    # Save SVG
    success = save_svg(args.filename, svg_content, validate=args.validate)

    return 0 if success else 1


if __name__ == '__main__':
    sys.exit(main())

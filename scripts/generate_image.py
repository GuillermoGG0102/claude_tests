#!/usr/bin/env python3
"""
AI Image Generation Script using OpenRouter

Generates or edits images using OpenRouter's image generation models.
Supports FLUX.2 Pro and Gemini 3 Pro.

Usage:
    python generate_image.py "A beautiful sunset over mountains"
    python generate_image.py "Make the sky purple" --input photo.jpg
    python generate_image.py "A cat in space" --model "black-forest-labs/flux.2-pro"
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path
from typing import Optional

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found.")
    print("Install it with: pip install requests")
    sys.exit(1)


def load_env_file(env_path: str = ".env") -> dict:
    """Load environment variables from .env file."""
    env_vars = {}
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    if "=" in line:
                        key, value = line.split("=", 1)
                        env_vars[key.strip()] = value.strip()
    return env_vars


def get_api_key(api_key_arg: Optional[str] = None) -> str:
    """Get OpenRouter API key from argument, env file, or environment."""
    if api_key_arg:
        return api_key_arg

    env_vars = load_env_file()
    if "OPENROUTER_API_KEY" in env_vars:
        return env_vars["OPENROUTER_API_KEY"]

    api_key = os.getenv("OPENROUTER_API_KEY")
    if api_key:
        return api_key

    print("Error: OpenRouter API key not found.")
    print("\nSetup options:")
    print("1. Create .env file with: OPENROUTER_API_KEY=your-key-here")
    print("2. Set environment variable: export OPENROUTER_API_KEY=your-key")
    print("3. Pass via command: --api-key your-key-here")
    print("\nGet API key from: https://openrouter.ai/keys")
    sys.exit(1)


def encode_image(image_path: str) -> str:
    """Encode image to base64 for API submission."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_image_media_type(image_path: str) -> str:
    """Get MIME type based on file extension."""
    ext = Path(image_path).suffix.lower()
    types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    return types.get(ext, "image/png")


def generate_image(
    prompt: str,
    model: str = "google/gemini-3-pro-image-preview",
    api_key: str = None,
    input_image: Optional[str] = None,
) -> Optional[str]:
    """Generate or edit an image using OpenRouter API."""
    api_key = get_api_key(api_key)

    url = "https://openrouter.ai/api/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://github.com/anthropics/claude-code",
        "X-Title": "Claude Image Generator",
    }

    if input_image:
        if not os.path.exists(input_image):
            print(f"Error: Input image not found: {input_image}")
            return None

        image_data = encode_image(input_image)
        media_type = get_image_media_type(input_image)

        body = {
            "model": model,
            "prompt": prompt,
            "images": [
                {
                    "url": f"data:{media_type};base64,{image_data}",
                }
            ],
        }
    else:
        body = {
            "model": model,
            "prompt": prompt,
        }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=120)
        response.raise_for_status()

        result = response.json()

        if "data" in result and len(result["data"]) > 0:
            return result["data"][0].get("url")
        elif "content" in result and len(result["content"]) > 0:
            return result["content"][0].get("data")

        print("Error: No image data in response")
        print(f"Response: {json.dumps(result, indent=2)}")
        return None

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Try again.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e.response.status_code}")
        try:
            error_data = e.response.json()
            if "error" in error_data:
                print(f"Details: {error_data['error']}")
        except Exception:
            print(f"Response: {e.response.text}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def save_image(image_data: str, output_path: str) -> bool:
    """Save image from URL or base64 data."""
    try:
        if image_data.startswith("http"):
            response = requests.get(image_data, timeout=30)
            response.raise_for_status()
            image_bytes = response.content
        else:
            image_bytes = base64.b64decode(image_data)

        with open(output_path, "wb") as f:
            f.write(image_bytes)

        print(f"✓ Image saved to: {output_path}")
        return True

    except Exception as e:
        print(f"Error saving image: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate or edit images using OpenRouter AI models"
    )
    parser.add_argument("prompt", help="Image generation or editing prompt")
    parser.add_argument(
        "-i",
        "--input",
        help="Input image path for editing (enables edit mode)",
    )
    parser.add_argument(
        "-m",
        "--model",
        default="google/gemini-3-pro-image-preview",
        help="OpenRouter model ID (default: google/gemini-3-pro-image-preview)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="generated_image.png",
        help="Output file path (default: generated_image.png)",
    )
    parser.add_argument(
        "--api-key",
        help="OpenRouter API key (overrides .env file)",
    )

    args = parser.parse_args()

    if args.input:
        print(f"🎨 Editing image: {args.input}")
        print(f"📝 Prompt: {args.prompt}")
    else:
        print(f"🎨 Generating image")
        print(f"📝 Prompt: {args.prompt}")

    print(f"🤖 Model: {args.model}")

    image_data = generate_image(
        prompt=args.prompt,
        model=args.model,
        api_key=args.api_key,
        input_image=args.input,
    )

    if image_data:
        save_image(image_data, args.output)
    else:
        print("❌ Failed to generate/edit image")
        sys.exit(1)


if __name__ == "__main__":
    main()

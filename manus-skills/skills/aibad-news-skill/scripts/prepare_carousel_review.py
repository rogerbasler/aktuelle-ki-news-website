#!/usr/bin/env python3
"""Prepare review assets for an AI Bad News Instagram carousel.

Usage:
  python prepare_carousel_review.py --input-dir /path/to/slides --output-dir /path/to/review --caption /path/to/caption.txt

Expected slide names in input-dir:
  slide_01.png ... slide_10.png

The script creates:
  - review/aibadnews_preview.jpg
  - review/aibadnews_carousel.zip
  - copied review slide images with stable names
  - copied caption.txt
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import zipfile

from PIL import Image, ImageDraw, ImageFont


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare AI Bad News carousel review package")
    parser.add_argument("--input-dir", required=True, help="Directory containing slide_01.png to slide_10.png")
    parser.add_argument("--output-dir", required=True, help="Directory for review assets")
    parser.add_argument("--caption", required=True, help="Caption text file")
    parser.add_argument("--prefix", default="aibadnews_carousel", help="Filename prefix")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    caption_path = Path(args.caption)
    output_dir.mkdir(parents=True, exist_ok=True)

    slide_paths = []
    for i in range(1, 11):
        src = input_dir / f"slide_{i:02d}.png"
        if not src.exists():
            raise FileNotFoundError(f"Missing required slide: {src}")
        dst = output_dir / f"{args.prefix}_slide_{i:02d}.png"
        shutil.copy2(src, dst)
        slide_paths.append(dst)

    if not caption_path.exists():
        raise FileNotFoundError(f"Missing caption file: {caption_path}")
    caption_dst = output_dir / "caption.txt"
    shutil.copy2(caption_path, caption_dst)

    thumb_w, thumb_h = 272, 340
    cols, rows = 5, 2
    margin = 24
    label_h = 34
    sheet_w = cols * thumb_w + (cols + 1) * margin
    sheet_h = rows * (thumb_h + label_h) + (rows + 1) * margin
    sheet = Image.new("RGB", (sheet_w, sheet_h), "#0a0f14")
    draw = ImageDraw.Draw(sheet)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except Exception:
        font = ImageFont.load_default()

    for idx, slide_path in enumerate(slide_paths):
        img = Image.open(slide_path).convert("RGB")
        img.thumbnail((thumb_w, thumb_h), Image.LANCZOS)
        col = idx % cols
        row = idx // cols
        x = margin + col * (thumb_w + margin)
        y = margin + row * (thumb_h + label_h + margin)
        bg = Image.new("RGB", (thumb_w, thumb_h), "#111111")
        bg.paste(img, ((thumb_w - img.width) // 2, (thumb_h - img.height) // 2))
        sheet.paste(bg, (x, y))
        draw.text((x, y + thumb_h + 8), f"Slide {idx + 1:02d}", fill="#00ff88", font=font)

    preview = output_dir / f"{args.prefix}_preview.jpg"
    sheet.save(preview, quality=92)

    zip_path = output_dir / f"{args.prefix}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in slide_paths:
            zf.write(p, p.name)
        zf.write(caption_dst, "caption.txt")
        zf.write(preview, preview.name)

    print(preview)
    print(zip_path)


if __name__ == "__main__":
    main()

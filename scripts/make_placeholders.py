"""
Generates soft, on-brand placeholder images so the site looks complete
before Mika's real photos are ready. Safe to delete this whole scripts/
folder once real photos are in place -- it's not needed for the live site.

To swap in a real photo later: just save the new photo with the EXACT
SAME filename into the images/ folder (same name, same folder), overwriting
the placeholder. No HTML/CSS editing required.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUT, exist_ok=True)

# Soft blush / neutral palette to match the site
PALETTE = [
    ((238, 220, 216), (214, 184, 178)),  # blush
    ((230, 225, 216), (201, 190, 173)),  # sand
    ((222, 224, 219), (186, 190, 178)),  # sage-grey
    ((236, 231, 224), (210, 198, 182)),  # warm taupe
]

def get_font(size):
    for path in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

def gradient(w, h, c1, c2):
    img = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    mask = Image.new("L", (w, h))
    mask_data = []
    for y in range(h):
        mask_data.extend([int(255 * (y / h))] * w)
    mask.putdata(mask_data)
    img.paste(top, (0, 0), mask)
    return img

def label(img, text, sub=None):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font = get_font(max(18, w // 22))
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((w - tw) / 2, (h - th) / 2 - (10 if sub else 0)), text, fill=(90, 78, 74), font=font)
    if sub:
        font2 = get_font(max(14, w // 34))
        bbox2 = draw.textbbox((0, 0), sub, font=font2)
        tw2 = bbox2[2] - bbox2[0]
        draw.text(((w - tw2) / 2, (h - th) / 2 + th + 6), sub, fill=(120, 108, 104), font=font2)
    return img

def make(name, w, h, palette_i, text, sub=None):
    c1, c2 = PALETTE[palette_i % len(PALETTE)]
    img = gradient(w, h, c1, c2)
    label(img, text, sub)
    img.save(os.path.join(OUT, name), quality=87)

def corner_label(img, text):
    """Small unobtrusive bottom-corner watermark, for images that get real
    text overlaid on top of them (like the hero banner)."""
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font = get_font(max(14, w // 60))
    draw.rectangle([0, h - 46, w, h], fill=(58, 51, 47))
    draw.text((20, h - 34), text, fill=(241, 226, 221), font=font)
    return img

def make_hero(name, w, h, palette_i, text):
    c1, c2 = PALETTE[palette_i % len(PALETTE)]
    img = gradient(w, h, c1, c2)
    corner_label(img, text)
    img.save(os.path.join(OUT, name), quality=87)

# Hero (home page) -- small corner watermark only, so it doesn't clash
# with the real headline text that displays on top of this image.
make_hero("hero.jpg", 1800, 1000, 0, "PLACEHOLDER: replace images/hero.jpg with a real 1800x1000px photo")

# Homepage hero slideshow (auto-cycles through these on the home page).
# Any number of slides works -- just keep the filenames matching what's
# referenced in index.html.
for i in range(1, 6):
    make_hero(f"hero-{i}.jpg", 1800, 1000, i,
              f"PLACEHOLDER: replace images/hero-{i}.jpg with a real 1800x1000px photo")

# About + Inquire headshot
make("headshot.jpg", 700, 700, 1, "Add headshot.jpg", "square photo, 700x700px")

# Portfolio grid (9 images across categories)
categories = ["Wedding", "Wedding", "Wedding", "Engagement", "Engagement",
              "Bridals", "Family", "Portrait", "Portrait"]
for i, cat in enumerate(categories, start=1):
    make(f"portfolio-{i}.jpg", 900, 1125, i, f"portfolio-{i}.jpg", cat)

# Reviews avatars (4)
for i in range(1, 5):
    make(f"review-{i}.jpg", 300, 300, i, f"review-{i}.jpg", "client photo")

print("Placeholder images created in", os.path.abspath(OUT))

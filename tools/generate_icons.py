"""Generate the green VND app icon for the Capacitor Android project.

Replaces the default Capacitor launcher icons with a green square,
white circle and a green VND sign, at the legacy and adaptive sizes
Capacitor expects. No binary assets are stored in the repo; this script
regenerates them on every cloud build.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = "android/app/src/main/res"
GREEN = (14, 138, 82, 255)
WHITE = (255, 255, 255, 255)


def font_for(size):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ):
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_icon(size, background, circle=True):
    img = Image.new("RGBA", (size, size), background)
    draw = ImageDraw.Draw(img)
    if circle:
        margin = int(size * 0.12)
        draw.ellipse([margin, margin, size - margin, size - margin], fill=WHITE)
        f = font_for(int(size * 0.55))
        text = "\u0111"
        bbox = draw.textbbox((0, 0), text, font=f)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((size - w) / 2 - bbox[0], (size - h) / 2 - bbox[1]),
                  text, font=f, fill=GREEN)
    return img


def main():
    legacy = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    adaptive = {
        "mipmap-mdpi": 108,
        "mipmap-hdpi": 162,
        "mipmap-xhdpi": 216,
        "mipmap-xxhdpi": 324,
        "mipmap-xxxhdpi": 432,
    }
    for folder, size in legacy.items():
        icon = draw_icon(size, GREEN)
        for name in ("ic_launcher.png", "ic_launcher_round.png"):
            icon.save(os.path.join(BASE, folder, name))
    for folder, size in adaptive.items():
        fg = draw_icon(size, (0, 0, 0, 0))
        fg.save(os.path.join(BASE, folder, "ic_launcher_foreground.png"))
    bg_path = os.path.join(BASE, "values/ic_launcher_background.xml")
    if os.path.exists(bg_path):
        with open(bg_path, encoding="utf-8") as fh:
            content = fh.read()
        content = content.replace("#FFFFFF", "#0E8A52").replace("#ffffff", "#0E8A52")
        with open(bg_path, "w", encoding="utf-8") as fh:
            fh.write(content)
    print("icons generated")


if __name__ == "__main__":
    main()

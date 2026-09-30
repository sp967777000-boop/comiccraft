from PIL import Image, ImageDraw
import os


def build_comic_layout(panel_paths, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    panels = []

    for path in panel_paths:
        if os.path.exists(path):
            panels.append(Image.open(path).convert("RGB"))

    if not panels:
        raise ValueError("No panel images found")

    width = 1024
    panel_height = 1024

    comic = Image.new(
        "RGB",
        (width, panel_height * len(panels)),
        "white"
    )

    y = 0

    for panel in panels:
        panel = panel.resize((width, panel_height))
        comic.paste(panel, (0, y))
        y += panel_height

    comic.save(output_path)

    return output_path
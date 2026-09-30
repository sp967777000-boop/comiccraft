import os
from PIL import Image, ImageDraw, ImageFont


def generate_image(image_prompt, panel_number):
    os.makedirs("static/panels", exist_ok=True)

    image_path = f"static/panels/panel_{panel_number}.png"

    # Temporary placeholder image
    image = Image.new("RGB", (1024, 1024), "white")
    draw = ImageDraw.Draw(image)

    draw.text(
        (50, 450),
        f"ComicCraft Panel {panel_number}\n\n{image_prompt[:150]}",
        fill="black"
    )

    image.save(image_path)

    return image_path
import io
import os
from PIL import Image


def open_image(image) -> bytes:
    an_image = Image.open(image)
    output = io.BytesIO()
    an_image.save(output, "jpeg")
    image_as_bytes = output.getvalue()
    return image_as_bytes


def listdir_fullpath(d: str) -> list[str]:
    return [os.path.join(d, f) for f in os.listdir(d)]

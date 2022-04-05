import io
import os
import shutil
from pathlib import Path
from typing import Union
from uuid import uuid4

import typer
from PIL import Image


def create_copies(path: Union[Path, str], n: int) -> None:
    cwd = Path(__file__).parent.resolve()
    image_folder = os.path.join(cwd, "images")
    filename = os.path.join(image_folder, path).split("\\")[-1]
    filename_raw = filename.split(".")[0]
    file_format = filename.split(".")[1]
    for index in range(n):
        new_filename = filename_raw + "_" + str(uuid4()) + "." + file_format
        try:
            shutil.copyfile(
                os.path.join(image_folder, filename),
                os.path.join(image_folder, new_filename),
            )
        except FileExistsError:
            raise typer.Exit(f"{new_filename} not found")
        except FileNotFoundError:
            raise typer.Exit(f"{filename} not found")


def open_image(image) -> bytes:
    an_image = Image.open(image)
    output = io.BytesIO()
    an_image.save(output, "jpeg")
    image_as_bytes = output.getvalue()
    return image_as_bytes


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

import os
from pathlib import Path
import shutil
from typing import Union


def create_copies(path: Union[Path, str], n: int = 100) -> None:
    cwd = Path(__file__).parent.resolve()
    image_folder = os.path.join(cwd, "images")
    filename = os.path.join(image_folder, path).split("\\")[-1]
    filename_raw = filename.split(".")[0]
    file_format = filename.split(".")[1]
    for index in range(n):
        new_filename = filename_raw + "_" + str(index) + "." + file_format
        try:
            shutil.copyfile(
                os.path.join(image_folder, filename),
                os.path.join(image_folder, new_filename),
            )
        except FileExistsError:
            print("File already exists")
        except FileNotFoundError:
            print("File found not")

    rename_files(image_folder)


def rename_files(file_path: Union[Path, str]) -> None:
    files = os.listdir(file_path)
    for index, file in enumerate(files):
        os.rename(
            os.path.join(file_path, file),
            os.path.join(file_path, "".join(["photo_", str(index), ".jpg"])),
        )


create_copies("photo.jpg", 10)

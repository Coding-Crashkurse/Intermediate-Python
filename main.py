import os
import time
from pathlib import Path

import typer

from database import database
from face_detection import bytestring_to_prediction, file_to_prediction
from helper import create_copies, listdir_fullpath, open_image

app = typer.Typer()


@app.command()
def copy_photo(path: str, n: int):
    create_copies(path, n)
    typer.echo(f"{path} was copied {n} times!")


@app.command()
def imgs_to_redis(
    subfolder: str = typer.Option("images", help="Subfolder where images lie...")
):
    start = time.perf_counter()
    cwd = Path(__file__).parent.resolve()
    img_folder = os.path.join(cwd, subfolder)
    files = listdir_fullpath(img_folder)
    typer.echo(f"{len(files)} files gefunden")
    for index, item in enumerate(files):
        bytes_ = open_image(item)
        filename = item.split("\\")[-1]
        database.set(name=filename, value=bytes_)
    end = time.perf_counter()
    typer.echo(
        f"Images erfolgreich in DB geschriebe. Dauer: {round(end-start,4)} Sekunden"
    )


@app.command()
def delete_from_redis():
    keys_count = database.dbsize()
    typer.echo(f"Zu löschende Einträge: {keys_count}")
    delete = typer.confirm("Are you sure you want to delete it?")
    if not delete:
        typer.echo("Not deleting")
        raise typer.Abort()
    for key in database.scan_iter():
        database.delete(key)
    typer.echo("Einträge wurden gelöscht")


@app.command()
def predict_from_redis():
    start = time.perf_counter()
    keys_count = database.dbsize()
    predict_bool = typer.confirm(f"{keys_count} Einträge gefunden. Prediction starten?")
    if not predict_bool:
        typer.echo("Not predicting")
        raise typer.Abort()
    for key in database.scan_iter():
        image = database.get(key)
        prediction = bytestring_to_prediction(image)
    end = time.perf_counter()
    typer.echo(f"Gesichter erfolgreich erkannt. Dauer: {round(end-start,4)} Sekunden")


@app.command()
def predict_from_disc(
    subfolder: str = typer.Option("images", help="Subfolder where images lie...")
):
    start = time.perf_counter()
    cwd = Path(__file__).parent.resolve()
    img_folder = os.path.join(cwd, subfolder)
    files = listdir_fullpath(img_folder)
    predict_bool = typer.confirm(f"{len(files)} Einträge gefunden. Prediction starten?")
    if not predict_bool:
        typer.echo("Not predicting")
        raise typer.Abort()
    for image in files:
        prediction = file_to_prediction(image)
    end = time.perf_counter()
    typer.echo(f"Gesichter erfolgreich erkannt. Dauer: {round(end-start,4)} Sekunden")


if __name__ == "__main__":
    app()

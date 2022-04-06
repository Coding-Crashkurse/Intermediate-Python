import os
import time
from pathlib import Path

import typer

from face_detection import file_to_prediction
from helper import listdir_fullpath

app = typer.Typer()


@app.command()
def help():
    typer.echo(
        "Verwende python main.py zur Erstellung von neuen Bildern mit erkannten Gesichtern"
    )


@app.command()
def predict(
    subfolder: str = typer.Option("images", help="Subfolder where images lie...")
):
    start = time.perf_counter()
    cwd = Path(__file__).parent.resolve()
    img_folder = os.path.join(cwd, subfolder)
    files = listdir_fullpath(img_folder)
    if len(files) == 0:
        typer.echo(f"Keine Bilder entdeckt. Bitte lege Bilder in {subfolder} ab")
        raise typer.Abort()
    predict_bool = typer.confirm(f"{len(files)} Einträge gefunden. Prediction starten?")
    if not predict_bool:
        typer.echo("Vorhersage abgebrochen")
        raise typer.Abort()
    for image in files:
        file_to_prediction(image)
    end = time.perf_counter()
    typer.echo(f"Gesichter erfolgreich erkannt. Dauer: {round(end-start,4)} Sekunden")


if __name__ == "__main__":
    app()

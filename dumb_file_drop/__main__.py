"""Simple server which accepts video file uploads"""

from pathlib import Path

from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = "srs bsnz"

(UPLOAD_FOLDER := Path("./uploads")).mkdir(parents=True, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Endpoint which processes a file upload or shows the upload form"""
    if not request.method == "POST":
        return render_template("index.html")

    # check if the post request has the file part
    if 'theFile' not in request.files:
        flash('ERROR: No file part')
        return redirect(request.url)

    file = request.files['theFile']

    # if user does not select file, browser also submit an empty part without filename
    if not file or not file.filename:
        flash('ERROR: No file uploaded')
    else:
        file.save(UPLOAD_FOLDER / secure_filename(file.filename))
        print(f"{file.filename} successfully uploaded!")
        flash(f"Successfully uploaded {file.filename}! 🐱")

    return redirect(request.url)


def _main() -> None:
    """Main driver to be run if this script is invoked directly."""
    app.run("0.0.0.0")


if __name__ == '__main__':
    _main()

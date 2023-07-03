"""Simple server which accepts video file uploads"""

import logging

from pathlib import Path

from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

log = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = "srs bsnz"

(UPLOAD_FOLDER := Path("./uploads")).mkdir(parents=True, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """Endpoint which processes a file upload or shows the upload form"""
    if not request.method == "POST":
        return render_template("index.html")

    if not (file := request.files.get('theFile')) or not file.filename:  # handle case where user submits empty form
        flash('ERROR: No file uploaded')
    else:
        file.save(UPLOAD_FOLDER / secure_filename(file.filename))
        log.info("'%s' was uploaded", file.filename)
        flash(f"Successfully uploaded {file.filename}! 🐱")

    return redirect(request.url)


def _main() -> None:
    """Main driver to be run if this script is invoked directly."""
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("{asctime}: {levelname}: {message}", "%Y-%m-%d %H:%M:%S", "{"))
    log.addHandler(handler)
    log.setLevel(logging.INFO)

    # app.run("0.0.0.0", 8000, True)
    app.run(debug=True)


if __name__ == '__main__':
    _main()

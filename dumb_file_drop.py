"""Simple server which accepts video file uploads"""

from pathlib import Path

from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = "super secret key"

UPLOAD_FOLDER = Path("./uploads")
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def upload_file():

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
    elif not file.filename.lower().endswith((".mov", "mp4", "txt")):
        flash('ERROR: Invalid file type')
    else:
        # print(f"Made it here: {file.filename}")
        # filename = secure_filename(file.filename)

        # print(f"Saving to {os.path.join(UPLOAD_FOLDER, filename)}")
        file.save(UPLOAD_FOLDER / secure_filename(file.filename))
        flash("Success!")
    return redirect(request.url)


app.run("0.0.0.0")

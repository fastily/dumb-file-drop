"""Main module, contains logic for web app"""

import logging

from pathlib import Path

import aiofiles
import uvicorn

from fastapi import FastAPI, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from rich.logging import RichHandler

_CHUNK_SIZE = 1024 * 1024 * 4

log = logging.getLogger(__name__)
log.addHandler(RichHandler(rich_tracebacks=True))
log.setLevel(logging.INFO)

app = FastAPI(title="Dumb File Drop", docs_url=None, redoc_url=None)

templates = Jinja2Templates("dumb_file_drop/templates")
(UPLOAD_FOLDER := Path("./uploads")).mkdir(parents=True, exist_ok=True)


def _sanitize_filename(fn: str) -> Path:
    """Convenience method, sanitizes file names and prefixes the return value with the `UPLOAD_FOLDER`

    Args:
        fn (str): The filename to sanitize

    Returns:
        Path: `fn`, sanitized and prefixed with `UPLOAD_FOLDER`.
    """
    return UPLOAD_FOLDER / fn.replace("/", "_").replace(":", "-")


@app.get("/file-exists")
async def file_exists(fn: str) -> dict[str, bool]:
    """Checks if a file with this name is already on the server.

    Args:
        fn (str): The name of the file to check

    Returns:
        dict[str, bool]: Some JSON indicating if the resopnse was successful.
    """
    return {"detail": _sanitize_filename(fn).is_file()}


@app.get("/")
async def show_index(request: Request) -> HTMLResponse:
    """Shows the web UI"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def upload(f: UploadFile) -> dict[str, str]:
    """File upload endpoint.

    Args:
        f (UploadFile): The file that was uploaded

    Returns:
        dict: Some JSON indicating if the operation was successful.
    """
    log.info("Now uploading '%s'...", sanitized_fn := _sanitize_filename(f.filename))

    if sanitized_fn.is_file():
        log.error("'%s' already exists, abort!", sanitized_fn)
        raise HTTPException(409, f"File already uploaded: {f.filename}")

    async with aiofiles.open(sanitized_fn, 'wb') as out_file:
        while content := await f.read(_CHUNK_SIZE):
            await out_file.write(content)

    log.info("Upload for '%s' complete!", sanitized_fn)

    return {"detail": "OK"}


if __name__ == '__main__':
    uvicorn.run("dumb_file_drop.__main__:app", reload=True)

"""Main module, contains logic for web app"""

import logging

from pathlib import Path

import aiofiles
import uvicorn

from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from rich.logging import RichHandler

_CHUNK_SIZE = 1024 * 1024 * 4

log = logging.getLogger(__name__)
app = FastAPI(title="Dumb File Drop", docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory="dumb_file_drop/templates")
(UPLOAD_FOLDER := Path("./uploads")).mkdir(parents=True, exist_ok=True)


@app.get("/")
async def get_index(request: Request) -> HTMLResponse:
    """Shows the web UI"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/")
async def post_index(f: UploadFile) -> dict[str, str]:
    """File upload endpoint.

    Args:
        f (UploadFile): The file that was uploaded

    Returns:
        dict: Some JSON indicating if the operation was successful.
    """
    log.info("Now uploading '%s'...", sanitized_fn := f.filename.replace("/", "_").replace(":", "-"))

    async with aiofiles.open(UPLOAD_FOLDER / sanitized_fn, 'wb') as out_file:
        while content := await f.read(_CHUNK_SIZE):
            await out_file.write(content)

    log.info("Upload for '%s' complete!", sanitized_fn)

    return {"detail": "OK"}


def _main() -> None:
    """Main driver, to be run if this module is invoked directly."""
    log.addHandler(RichHandler(rich_tracebacks=True))
    log.setLevel(logging.INFO)

    uvicorn.run("dumb_file_drop.__main__:app", reload=True)


if __name__ == '__main__':
    _main()

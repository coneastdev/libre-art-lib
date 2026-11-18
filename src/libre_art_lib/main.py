from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

package_dir = Path(__file__).parent

app.mount(
    "/static",
    StaticFiles(directory=package_dir / "static"),
    name="static",
)


templates = Jinja2Templates(directory=package_dir / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/search/", response_class=HTMLResponse)
async def blank_search(request: Request):
    return templates.TemplateResponse(
        request=request, name="search.html", context={"q": ""}
    )

@app.get("/search/{q}", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse(
        request=request, name="search.html", context={"query": q}
    )
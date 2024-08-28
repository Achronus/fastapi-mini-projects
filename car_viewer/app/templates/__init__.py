from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="", include_in_schema=False)


@router.get("/", response_class=RedirectResponse)
def home(request: Request):
    return RedirectResponse("/cars")

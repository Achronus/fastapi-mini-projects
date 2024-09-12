from fastapi import APIRouter
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="", include_in_schema=False)


@router.get("/")
def home():
    return {"test": "test"}

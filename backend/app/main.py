from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .api.endpoints import router as estudio_router

app = FastAPI()

# Montar los archivos estáticos
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Configurar las plantillas de Jinja2
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(estudio_router)

@app.on_event("startup")
async def startup_event():
    from .db.database import engine
    from .models.models import Base
    Base.metadata.create_all(bind=engine)

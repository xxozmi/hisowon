from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.stasticfiles import staticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI
app.mount("/static", Sta)

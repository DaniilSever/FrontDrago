from fastapi import FastAPI
from .domain import routers

app = FastAPI()

for router in routers:
    app.include_router(router)
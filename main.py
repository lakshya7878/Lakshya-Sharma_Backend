from fastapi import FastAPI
from routes.trade_routes import client

app = FastAPI()
app.include_router(client)


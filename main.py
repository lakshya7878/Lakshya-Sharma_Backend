from fastapi import FastAPI
from routes.trade_routes import client
from fastapi_pagination import Page, add_pagination, paginate


app = FastAPI()
app.include_router(client)

add_pagination(app) 
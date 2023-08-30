from fastapi import FastAPI
from routes import customers

fast_api = FastAPI(prefix="/api/v1")
fast_api.include_router(customers.router, prefix="/customers")
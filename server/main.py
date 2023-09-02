from fastapi import FastAPI
from routes import customers
from data.database import prisma

fast_api = FastAPI()
fast_api.include_router(customers.router)

@fast_api.on_event("startup")
async def startup():
    await prisma.connect()

@fast_api.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

@fast_api.get("/")
def read_root():
    return {"version": "1.0.2"}
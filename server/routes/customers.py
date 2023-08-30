from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import List
from data.database import ActivePrismaClient
from schemas import schemas
from services import customers as service

# Create our API router
router = APIRouter()

# Create a dependency for our database connection
async def get_db_session():
    try:
        db = await ActivePrismaClient().connect()
        yield db
    finally:
        await db.disconnect()

@router.get(
    "/",
    response_model=List[schemas.Customer],
    summary="Get all customers"
)
def get_all_customers(db: ActivePrismaClient = Depends(get_db_session)):
    return service.get_all_customers(db)


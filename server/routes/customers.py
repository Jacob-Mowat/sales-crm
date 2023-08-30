from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import List
from data.database import ActivePrismaClient
from schemas.customer import Customer
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
    response_model=List[Customer],
    summary="Get all customers"
)
def get_all_customers(db: ActivePrismaClient = Depends(get_db_session)):
    return service.retrieve_all_customers(db)


@router.get(
    "/{customer_id}",
    response_model=Customer,
    summary="Get a customer by ID"
)
def get_customer_by_id(
    customer_id: int = Path(..., gt=0),
    db: ActivePrismaClient = Depends(get_db_session)
):
    return service.retrieve_customer_by_id(db, customer_id)


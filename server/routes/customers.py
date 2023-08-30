from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import List
from schemas.customer import Customer
from services import customers as service
import asyncio

# Create our API router
router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)

@router.get(
    "/",
    response_model=List[Customer],
    summary="Get all customers"
)
async def get_all_customers():
    return await service.retrieve_all_customers()
    


@router.get(
    "/{customer_id}",
    response_model=Customer,
    summary="Get a customer by ID"
)
async def get_customer_by_id(
    customer_id: int = Path(..., gt=0),
):
    return await service.retrieve_customer_by_id(customer_id)


from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import List
from schemas.customer import CreateCustomer, Customer
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
    status_code=status.HTTP_200_OK,
    summary="Get a customer by ID"
)
async def get_customer_by_id(
    customer_id: int = Path(..., gt=0),
):
    customer = await service.retrieve_customer_by_id(customer_id)
    
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    else:
        return customer

@router.post(
    "/",
    response_model=Customer,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new customer"
)
async def create_customer(
    customer: CreateCustomer
):
    serviceResponse = await service.create_customer(customer)

    if serviceResponse is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer could not be created"
        )
    else:
        return serviceResponse
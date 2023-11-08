from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import List
from schemas.customer import CreateCustomer, Customer, CreateCustomerContact, CustomerContact, UpdateCustomer
from services import customers as customers_service
from services import customercontacts as customercontacts_service
import asyncio

# Create our API router
router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
)

# Get ALL Customers
@router.get(
    "/",
    response_model=List[Customer],
    summary="Get all customers"
)
async def get_all_customers():
    return await customers_service.retrieve_all_customers()

# Get a Customer by ID
@router.get(
    "/{customer_id}",
    response_model=Customer,
    status_code=status.HTTP_200_OK,
    summary="Get a customer by ID"
)
async def get_customer_by_id(
    customer_id: int = Path(..., gt=0),
):
    customer = await customers_service.retrieve_customer_by_id(customer_id)
    
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    else:
        return customer

# Create a new Customer
@router.post(
    "/",
    response_model=Customer,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new customer"
)
async def create_customer(
    customer: CreateCustomer
):
    serviceResponse = await customers_service.create_customer(customer)

    if serviceResponse is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer could not be created"
        )
    else:
        return serviceResponse
    
# Update a Customer
@router.post(
    "/{customer_id}",
    response_model=Customer,
    status_code=status.HTTP_200_OK,
)
async def update_customer(
    customer: UpdateCustomer,
    customer_id: int = Path(..., gt=0)
):
    serviceResponse = await customers_service.update_customer(customer_id, customer)

    if serviceResponse is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer could not be updated"
        )
    else:
        return serviceResponse
    
# Create a new CustomerContact and connect it to a Customer
@router.post(
    "/{customer_id}/create-contact",
    response_model=CustomerContact,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new customer contact and connect it to a customer"
)
async def create_customer_contact(
    contact: CreateCustomerContact,
    customer_id: int = Path(..., gt=0)
):
    serviceResponse = await customers_service.create_customer_contact(customer_id, contact)

    if serviceResponse is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer contact could not be created"
        )
    else:
        return serviceResponse
    
    
@router.delete(
    "/{customer_id}/delete-contact/{contact_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a customer contact"
)
async def delete_customer_contact(
    customer_id: int = Path(..., gt=0),
    contact_id: int = Path(..., gt=0)
):
    print(f"[DEBUG] customer_id: {customer_id}")
    print(f"[DEBUG] contact_id: {contact_id}")
    
    # Confirm that the Customer owns the CustomerContact, and also that the CustomerContact exists
    # If not, raise an HTTPException
    customer: Customer = await customers_service.retrieve_customer_by_id(customer_id)
    
    if customer is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    
    contact: CustomerContact = await customercontacts_service.retrieve_customer_contact_by_id(contact_id)
    
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer contact not found"
        )
        
    if contact.customerId != customer_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer does not own this contact"
        )
    
    # If the Customer owns the CustomerContact, delete it
    serviceResponse = await customers_service.delete_customer_contact(customer_id, contact_id)

    if serviceResponse is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Customer contact could not be deleted"
        )
    else:
        return serviceResponse
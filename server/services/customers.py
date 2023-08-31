from data.database import prisma
from prisma.models import Customer

async def retrieve_all_customers():
    return await prisma.customer.find_many()

async def retrieve_customer_by_id(customer_id: int):
    return await prisma.customer.find_first(where={"id": customer_id})

async def create_customer(customer: CreateCustomer):
    return await prisma.customer.create(customer)
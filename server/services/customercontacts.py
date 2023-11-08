from data.database import prisma
from schemas.customer import CreateCustomer, Customer, CreateCustomerContact, CustomerContact, UpdateCustomer
from typing import Union

async def retrieve_all_customer_contacts():
    return await prisma.customercontact.find_many()

async def retrieve_customer_contact_by_id(customer_contact_id: int):
    try:
        return await prisma.customercontact.find_first(where={"id": customer_contact_id})
    except Exception as e:
        print(e)
        return None
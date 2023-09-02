from data.database import prisma
from schemas.customer import CreateCustomer, Customer, CreateCustomerContact, CustomerContact
from typing import Union

async def retrieve_all_customers():
    return await prisma.customer.find_many()

async def retrieve_customer_by_id(customer_id: int):
    try:
        return await prisma.customer.find_first(where={"id": customer_id})
    except Exception as e:
        print(e)
        return None
    
async def create_customer(customer: CreateCustomer) -> Union[Customer, None]:
    try :
        data: Customer = await prisma.customer.create(customer.__dict__)
        return data
    except Exception as e:
        print(e)
        return None
    
async def create_customer_contact(customer_id: int, customer_contact: CreateCustomerContact) -> Union[CustomerContact, None]:
    try :
        _cc = customer_contact.__dict__
        _cc["customerId"] = customer_id 
        data: CustomerContact = await prisma.customercontact.create(_cc)
        return data
    except Exception as e:
        print(e)
        return None
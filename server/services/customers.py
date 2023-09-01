from data.database import prisma
from schemas.customer import CreateCustomer, Customer

async def retrieve_all_customers():
    return await prisma.customer.find_many()

async def retrieve_customer_by_id(customer_id: int):
    return await prisma.customer.find_first(where={"id": customer_id})

async def create_customer(customer: CreateCustomer):
    try :
        data: Customer = await prisma.customer.create(customer)
        print(data.name)
        return data
    except Exception as e:
        print(e)
        return None

    return data
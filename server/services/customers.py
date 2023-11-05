from data.database import prisma
from schemas.customer import CreateCustomer, Customer, CreateCustomerContact, CustomerContact, UpdateCustomer
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
    
async def update_customer(customer_id: int, customer: UpdateCustomer) -> Union[Customer, None]:
    updated: bool = False
    
    name: str = customer.__dict__['name']
    notes: str = customer.__dict__['notes']
    
    print(f"[DEBUG] name: {name}")
    print(f"[DEBUG] notes: {notes}")
    
    try:
        if name:
            updated_name: Customer = await prisma.customer.update(
                where={
                    'id': customer_id
                },
                data={
                    'name': name
                }
            )
            
            updated = True
        
        if notes:
            updated_notes: Customer = await prisma.customer.update(
                where={
                    'id': customer_id
                },
                data={
                    'notes': notes
                }
            )
            
            updated = True
            
        if updated:
            return await prisma.customer.find_first(where={"id": customer_id})
        else:
            return None
        
    except Exception as e:
        print(f"[ERROR] {e}")
        return None
    
async def create_customer_contact(customer_id: int, customer_contact: CreateCustomerContact) -> Union[CustomerContact, None]:
    try :
        # Set the customerId to the one provided in the path
        _cc = customer_contact.__dict__
        _cc["customerId"] = customer_id 
        
        # Create the CustomerContact
        data: CustomerContact = await prisma.customercontact.create(_cc)
        
        return data
    except Exception as e:
        print(e)
        return None
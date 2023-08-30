from prisma.models import Customer

def retrieve_all_customers(db):
    return db.customer.find_many()

def retrieve_customer_by_id(db, customer_id: int):
    return db.customer.find_first(where={"id": customer_id})
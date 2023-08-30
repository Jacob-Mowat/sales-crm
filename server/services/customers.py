from prisma.models import Customer

def retrieve_all_customers(db):
    return db.customer.find_many()
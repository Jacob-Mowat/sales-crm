from pydantic import BaseModel
from typing import Optional

"""
model Customer {
  id Int @id @default(autoincrement())

  name     String
  notes    String?
  phone    String?
  telegram String?
  snapchat String?

  // Relationships
  referredBy CustomerReferral?  @relation("ReferredBy")
  referredTo CustomerReferral[] @relation("ReferredTo")

  createdAt      DateTime       @default(now())
  updatedAt      DateTime       @updatedAt
  orders         Order[]
  orderAddresses OrderAddress[]
}

"""
class Customer(BaseModel):
    id: Optional[int] = None
    name: str
    notes: Optional[str] = None
    phone: Optional[str] = None
    telegram: Optional[str] = None
    snapchat: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    class Config:
        orm_mode = True
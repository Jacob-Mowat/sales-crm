from pydantic import BaseModel, Field
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
    id: Optional[int] = Field(None, alias="id")
    name: str = Field(..., alias="name")
    notes: Optional[str] = Field(None, alias="notes")
    createdAt: Optional[object] = Field(None, alias="createdAt")
    updatedAt: Optional[object] = Field(None, alias="updatedAt")

    class Config:
        orm_mode = True


class CreateCustomer(BaseModel):
    name: str = Field(..., alias="name")
    notes: Optional[str] = Field(None, alias="notes")


    class Config:
        orm_mode = True
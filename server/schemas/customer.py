from pydantic import BaseModel, Field
from typing import Optional


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
        
class CustomerContact(BaseModel):
    id: int = Field(None, alias="id")
    type: str = Field(..., alias="type")
    value: str = Field(..., alias="value")
    customerId: int = Field(..., alias="customerId")
    createdAt: Optional[object] = Field(None, alias="createdAt")
    updatedAt: Optional[object] = Field(None, alias="updatedAt")

    class Config:
        orm_mode = True
        
class CreateCustomerContact(BaseModel):
    type: str = Field(..., alias="type")
    value: str = Field(..., alias="value")

    class Config:
        orm_mode = True
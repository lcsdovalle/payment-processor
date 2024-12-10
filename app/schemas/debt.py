# app/models/customer_payment.py
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, field_validator


class CustomerDebt(BaseModel):
    debt_id: UUID = Field(..., description="Customers' debt id")
    email: EmailStr = Field(..., description="Customers' email")
    amount: Decimal = Field(
        ..., gt=0, description="This shold be > 0"
    )
    customer_name: str = Field(..., description="Customer's name")

    # https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.field_validator
    @field_validator("debt_id", mode="before")
    @classmethod
    def ensure_uuid_format(cls, v):
        take_out_piece = "\xa0"
        if take_out_piece in v:
            v = v.replace("\xa0", "")
        return v

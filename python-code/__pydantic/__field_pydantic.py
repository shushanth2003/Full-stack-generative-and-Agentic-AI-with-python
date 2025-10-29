from pydantic import BaseModel,Field;
from typing import List,Dict,Optional;

class Employee(BaseModel):
    employee_name:str=Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Shushanth B S"
    ),
    department:str=Field(
        ge=5,
        le=20
    ),
    salary:int=Field(
        ge=10000,
        le=20000
    )

class User(BaseModel):
    email: str = Field(
        ...,
        pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    )
    phone: str = Field(
        ...,
        min_length=10,
        max_length=10
    )

from pydantic import BaseModel;
from typing import List,Optional;

class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:str
    address:Address

address_=Address(
    street="Anna Nagar",
    city="Chennai",
    postal_code="637211"
);

user=User(
    id=1,
    name="shushanth",
    address=address_
);

user_={
    "id":1,
    "name":"shushanth",
    "address":{
        "street":"Anna Palace",
        "city":"Trichy",
        "postal_code":"637211"
    }
}

user_input=User(**user_);
print(user_input)
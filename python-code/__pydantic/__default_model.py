from pydantic import BaseModel;

class User(BaseModel):
    id:int
    name:str
    price:int
    in_stock:bool=False;


#create the input field

product_one={"id":1,"name":"mouse","price":400,"in_stock":True};

product_two={"id":2,"name":"keyboard","price":600,"in_stock":False};

product_one_input=User(**product_one);
product_two_input=User(**product_two);

print(product_one_input);
print(product_two_input);
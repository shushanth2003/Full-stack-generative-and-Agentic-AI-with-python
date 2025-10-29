from pydantic import BaseModel;

#create a data model
class User(BaseModel):
    id:int
    name_:str
    is_active:bool

#nput data
input_data={"id":101,"name_":"shushanth","is_active":False};

#initialize the variable
user=User(**input_data); #unpack a variables

#we need to analysis the data whether it fit or not
print(user);
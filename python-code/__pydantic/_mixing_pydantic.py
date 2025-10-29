from pydantic import BaseModel;
from typing import List,Optional,Dict;
class Cart(BaseModel):
    user_id:int
    items:List[str]
    quantities:Dict[str,int]

class Blogpost(BaseModel):
    title:str
    content:str
    image_url:Optional[str]=None #default conversion


cart_input={
    "user_id":1,
    "items":["mouse","keyboard","laptop"],
    "quantities":{
        "mouse":1,
        "keyboard":2,
        "laptop":3
    }
};

cart=Cart(**cart_input);

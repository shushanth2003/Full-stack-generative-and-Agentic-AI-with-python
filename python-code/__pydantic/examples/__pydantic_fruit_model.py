from typing import Annotated,Literal;
from pydantic import BaseModel;
from annotated_types import Gt;
class Fruit(BaseModel):
    name:str
    color:Literal["red","green"];
    weight:Annotated[float,Gt];
    bazam: dict[str, list[tuple[int, bool, float]]]


print(Fruit(
    name="Shushanth",
    color="green",
    weight=4.5,
    bazam={
    "footbar": [(1, True, 0.1)]
    }
))
from pydantic import BaseModel;
from typing import List,Optional;

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['comment']]=None;

Comment.model_rebuild();
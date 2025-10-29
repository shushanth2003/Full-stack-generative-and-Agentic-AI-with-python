from pydantic import BaseModel,Field,field_validator,model_validator;

class User(BaseModel):
    username:str

    @field_validator("username")
    def username_validation(cls,v):
        if(len(v)<4):
            raise ValueError("User Name should be greater than 4");
        return v;

class Signup(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode="after")
    def check_password(cls,values):
        if(values.password!=values.confirm_password):
            raise ValueError("Password doesn't match it");
        return values;
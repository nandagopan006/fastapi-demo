
from pydantic import BaseModel


class Product(BaseModel):
    id : int 
    title : str
    decs: str
    stock: int 
    price : int 


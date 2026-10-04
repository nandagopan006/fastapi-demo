from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greets():
    return "weellcome to learn fastapi"

products = [
    Product(id=1, title="Phone", decs="A smartphone", stock=50, price=699),
    Product(id=2, title="Laptop", decs="A powerful laptop", stock=30, price=999),
    Product(id=5, title="Pen", decs="A blue ink pen", stock=100, price=145),
    Product(id=6, title="Table", decs="A wooden table", stock=20, price=199),
]

@app.get("/products/")
def Products():
    return products

@app.get("/product/{id}/")
def product_get_by_id(id:int):
    for i in products:
        if i.id == id :
            return i
        
    return "Not a product unavabile here"

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

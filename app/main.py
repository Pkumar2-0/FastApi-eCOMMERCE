from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException, Query,Path
from app.services.product import get_all_products,add_product,delete_product,change_product
from app.schema.product import Product
from uuid import  UUID,uuid4
from datetime import datetime

load_dotenv()
app = FastAPI()

@app.get("/")
def root():
    return {"message": "welcome to fast api."}

# @app.get("/pro")
# def getpro():
#     return get_all_products();

@app.get("/product")
def list_products(
    name: str | None = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="search by product name (case insensitive)",
    ),
    sort_by_price:bool=Query(default=False,description=" Sort products by price"),
    order:str=Query(
        default="asc",description="sort order when sort_by_price=true(asc,desc)"
    ), 
    limit:int=Query(
        default=10,
        ge=1,
        le=100,
        description="Number of items to return",
    ),
    offset:int=Query(
        default=0,
        ge=0,
        description="pagination offset",
    ),
):
    products = get_all_products()
    

    if name:
        needle = name.strip().lower()
        products = [
            p for p in products if needle in p.get("name","").lower()
            
        ]

        if not products:
            raise HTTPException(
                status_code=404,
                detail=f"No Product found matching name={name}"
            )
    if sort_by_price:
        reverse=order=="desc"
        products=sorted(products, key=lambda p: p.get(" price",0),reverse=reverse)
    total = len(products)

    products=products[offset:offset+limit]

    return {
        "total": total,
        "items": products
    }


@app.get("/products/{product_id}")
def get_product_by_id(
    product_id:str =Path(
        ...,
        min_length=36,
        max_length=36,
        description="UUID of the products",
        examples="0005a4ea-ce3f-4dd7-bee0-f4ccc70fea6a"
    )
):
    products=get_all_products()
    for product in products:
        if product["id"]==product_id:
            return product
    raise HTTPException(status_code=404,detail=" product not found!")    

@app.post("/products")
def create_product(product: Product):
    product_dict=product.model_dump(mode="json")
    product_dict["id"]=str(uuid4())
    product_dict["created_at"]=datetime.utcnow().isoformat()+"z"
    try:
        add_product(product_dict)
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))    
    return product.model_dump(mode="json") 

@app.delete("/products/{product_id}")
def delete_product_by_id(product_id: UUID=Path(...,description="UUID of the product to delete")):
    try:
        result=delete_product(str(product_id))
        return result
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e))
    
    
@app.put("/products/{product_id}")
def update_product_by_id(
    product_id: UUID=Path(...,description="UUID of the product to update"),
    updated_product: Product=None
):
    updated_fields=updated_product.model_dump(exclude_unset=True)
    if not updated_fields:
        raise HTTPException(status_code=400,detail="No fields to update")
    try:
        result=change_product(str(product_id),updated_fields)
        return result
    except ValueError as e:
        raise HTTPException(status_code=404,detail=str(e)) 


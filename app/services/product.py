import json
from pathlib import Path
from typing import List, Dict

DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "dummy.json"



def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_products() -> List[Dict]:
    return load_products()


def save_product(products: List[Dict])-> None:
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(products,f,indent=2,ensure_ascii=False)

def add_product(product:dict)->dict:
    products=get_all_products()
    if any(p["sku"]==product["sku"] for p in products):
        raise ValueError("SKU already exists")
    products.append(product)
    save_product(products)
    return product

def delete_product(product_id:str)->None:
    products=get_all_products()
    for idx,p in enumerate(products):
        if p["id"]==product_id:
            deleted= products.pop(idx)
            save_product(products)
            return{"message":f"Product with id {product_id} deleted successfully","deleted_product":deleted}
    raise ValueError("Product not found")

def change_product(product_id:str,updated_fields:dict)->dict:
    products=get_all_products()
    for index,product in enumerate(products):
        if product["id"]==product_id:
            for key,value in updated_fields.items():
                if value in None:
                   continue

                if isinstance(value,dict) and isinstance(product.get(key),dict):
                    product[key].update(value)
                else:
                    product[key]=value
            products[index]=product    

            save_product(products)
            return products[index]
    raise ValueError("Product not found")
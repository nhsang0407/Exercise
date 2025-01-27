from Exercise_KTLT.Ex62.models.Category import Category
from Exercise_KTLT.Ex62.models.Product import Product


def enter_category():
    id=input("Enter category id: ")
    name=input("Enter category name: ")
    print("-"*30)
    category=Category(id,name)
    return category
def enter_product():
    id = input("Enter product id: ")
    name = input("Enter product name: ")
    price=input("Enter product price: ")
    madein=input("Enter product origin: ")
    product=Product(id,name,price,madein)
    print("-" * 30)
    return product
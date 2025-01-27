from Exercise_KTLT.Ex62.test.libs import enter_category, enter_product

list=[]
category=int(input("Enter number of category: "))
for i in range(category):
    list.append(enter_category())
for c in list:
    product=int(input(f"Enter number of product in category {c.name}: "))
    for j in range(product):
        c.add_product(enter_product())

print("Danh sách mục của cửa hàng:")
for c in list:
    print("Category:",c)
    for p in c.list_products:
        print(p)
    print("-"*30)

#update product
print("Update product:")
category_id = input("Enter category id: ")
product_id = input("Enter product id to update: ")
name = input("Enter new name: ")
price = input("Enter new price: ")
madein = input("Enter new origin: ")
for c in list:
    if c.id == category_id:
        print("Product is updated:",end=' ')
        print(c.update_product(product_id, name, price, madein))
        break
print("-"*30)
#delete product
print("Delete product:")
category_id = input("Enter category id: ")
product_id = input("Enter product id to delete: ")
for c in list:
    if c.id == category_id:
        print(c.delete_product(product_id))
        break
print("-"*30)
print("Total value of product:")
category_id = input("Enter category id: ")
for c in list:
    if c.id == category_id:
        print(f"Total value of items: {c.total_value()}")
print("-"*30)
origin = input("Enter country: ")
for c in list:
    products = c.list_products_by_origin(origin)
    print(f"Products in category {c.name} from {origin}:")
    for product in products:
        print(product)
class Category:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.list_products=[]
    def __str__(self):
        return f"{self.id}\t{self.name}"

    def add_product(self,p):
        self.list_products.append(p)

    def update_product(self, product_id, name=None, price=None, madein=None):
        for product in self.list_products:
            if product.id == product_id:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if madein:
                    product.madein = madein
                return f"{product_id}\t{name}\t{price}\t{madein}"
        return f"Product {product_id} not found."

    def delete_product(self, product_id):
        for product in self.list_products:
            if product.id == product_id:
                self.list_products.remove(product)
                return f"Product {product_id} deleted successfully."
        return f"Product {product_id} not found."

    def total_value(self):
        s=0
        for product in self.list_products:
            s=s+float(product.price)
        return s

    def list_products_by_origin(self, origin):
        return [product for product in self.list_products if product.madein == origin]


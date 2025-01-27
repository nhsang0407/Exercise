class Product:
    def __init__(self,id,name,price,madein):
        self.id=id
        self.name=name
        self.price=price
        self.madein=madein
    def __str__(self):
        infor=f"{self.id}\t{self.name}\t{self.price}\t{self.madein}"
        return infor
    def list_product_madein_country(self,origin):
        if self.madein==origin:
            return self


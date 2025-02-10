from Exercise_KTLT.Ex63.models.Product import Product


class NonOfficialProduct(Product):
    def __init__(self,id:str=None,name:str=None,price:float=None):
        super().__init__(id,name,price,discount=0.08,tax=0.0)
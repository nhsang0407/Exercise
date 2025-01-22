class Employee:
    def __init__(self,last_name,first_name,number_of_products):
        self.__last_name=last_name
        self.__first_name=first_name
        self.__number_of_products=number_of_products
    def __str__(self):
        if self.__number_of_products<0:
            self.__number_of_products=0
        return f"{self.__last_name}\t{self.__first_name}\t{self.__number_of_products}"

    def get_last_name(self):
        return self.__last_name
    def get_first_name(self):
        return self.__first_name
    def get_number_of_products(self):
        return self.__number_of_products
    def set_last_name(self,new_last_name):
        self.__last_name=new_last_name
    def set_first_name(self,new_first_name):
        self.__first_name=new_first_name
    def set_number_of_products(self,new_number_of_products):
        self.__number_of_products=new_number_of_products
    last_name=property(get_last_name,set_last_name)
    first_name=property(get_first_name,set_first_name)
    number_of_products=property(get_number_of_products,set_number_of_products)

    def get_salary(self):
        if self.__number_of_products<=199:
            salary=self.__number_of_products*0.5
        elif self.__number_of_products<=399:
            salary=self.__number_of_products*0.55
        elif self.__number_of_products<=599:
            salary=self.__number_of_products*0.6
        else:
            salary = self.__number_of_products * 0.65
        return salary

    def IsHigher(self,emp2):
        if self.__number_of_products>emp2.number_of_products:
            return True
        else:
            return False
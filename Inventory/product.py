class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self,value):
        if value < 0:
            print('La cantidad no puede ser negativa')
            self._quantity = 0
        else:
            self._quantity = value

class Electronic(Product):
    def __init__(self,name,price, quantity,warranty_months):
        super().__init__(name,price,quantity)
        self.warranty_months = warranty_months
    
    def __str__(self):
        return f"{super().__str__()}, Warranty: {self.warranty_months} months"

class Clothing(Product):
    def __init__(self,name,price, quantity,size):
        super().__init__(name,price,quantity)
        self.size = size
    
    def __str__(self):
        return f"{super().__str__()}, size: {self.size}"
class Inventory:
    def __init__(self):
        self.products = {}

    
    def add_product(self, product):
        if product.name in self.products:
            print("El producto ya existe")
            return
        self.products[product.name] = product
        print("Producto guardado exitósamente")
    
    def update_product(self, name,price=None,quantity=None):
        if name not in self.products:
            print("Ese producto no está en el inventario")
            return
        if price is not None:
            self.products[name].price = price
        if quantity is not None:
            self.products[name].quantity = quantity
        
        print("Producto se actualizó correctamente")
    
    def remove_product(self,name):
        if name not in self.products:
            print("Ese producto no existe")
            return
        del self.products[name]
        print("Producto removido exitósamente")
    
    def display_inventory(self):
        if not self.products:
            print("Inventario vacio")
            return
        for prod in self.products.values():
            print(prod)
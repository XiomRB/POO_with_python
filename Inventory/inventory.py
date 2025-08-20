import csv
from product import *

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
    
    def load_products_from_csv(self,file_name):
        try:
            with open(file_name,newline='',encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product_type = row['type'].lower()
                    name = row['product']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    if product_type == 'electronic':
                        warranty_months = row.get('warranty_months',0)
                        product = Electronic(name, price, quantity,warranty_months)
                    elif product_type == 'size':
                        size = row.get('size','U')
                        product = Clothing(name,price,quantity,size)
                    else:
                        product = Product(name,price,quantity)
                    
                    self.add_product(product)
        except FileNotFoundError:
            print(f"El archivo {file_name} no existe")
        except Exception as e:
            print(f'Hubo un error al abrir el archivo: {e}')
from product import Electronic, Clothing
from inventory import Inventory

if __name__ == "__main__":
    product = Electronic('Laptop', 10000, -10, 4)
    jacket = Clothing('Jacket', 250, 5, 'M')
    print(product, jacket)

    inventory = Inventory()
    inventory.add_product(product)
    inventory.add_product(jacket)
    inventory.display_inventory()
    
    inventory.update_product('Laptop',8500,2)
    pants = Clothing('Pants', 150, 10, 'L')
    inventory.add_product(pants)
    inventory.remove_product('Laptop')

    inventory.display_inventory()

    inventory.load_products_from_csv('products.csv')
    inventory.display_inventory()
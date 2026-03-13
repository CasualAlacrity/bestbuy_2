from typing import List

from products import Product

class Store:
    def __init__(self, products:List[Product]):
        self.products = products

    def add_product(self, product:Product):
        if type(product) is not Product:
            raise TypeError

        self.products.append(product)

    def remove_product(self, product:Product):
        if type(product) is not Product:
            raise TypeError
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.quantity

        return total

    def get_all_products(self) -> List[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list) -> float:
        order_total = 0

        for product, quantity in shopping_list:
            order_total += product.buy(quantity)

        return order_total
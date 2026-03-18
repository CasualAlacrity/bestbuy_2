from typing import List

from product import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = list(products)

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")

        self.products.append(product)

    def remove_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")

        self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            total += product.get_quantity()

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

class Product:
    def __init__(self, name:str, price:float, quantity:int):
        if name == "":
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")

        self.name = name
        self.price = price
        self.set_quantity(quantity)

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity:int):
        if (quantity < 0):
            raise ValueError("Product quantity cannot be negative")

        self.quantity = quantity

        if(self.quantity > 0):
            self.activate()
        else:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        # "MacBook Air M2, Price: 1450, Quantity: 100"
        # I checked, and it seems that this function was not intended to return a value. Weird.
        print(self.name, "Price:", self.price, "Quantity:", self.quantity)

    def buy(self, quantity) -> float:
        if (self.get_quantity() < quantity):
            raise ValueError("Not enough items in stock.")

        self.set_quantity(self.get_quantity() - quantity)
        return float(self.price * quantity)


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def show(self):
        print(self.name, "Price:", self.price, "Quantity: Unlimited")

    def set_quantity(self, quantity:int):
        super().quantity = 0

    def buy(self, quantity) -> float:
        return float(self.price * quantity)


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum:int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        print(self.name, "Price:", self.price, "Quantity:", self.quantity, "Maximum:", self.maximum, " (Per Order)")

    def buy(self, quantity) -> float:
        if self.get_quantity() > self.maximum:
            raise ValueError("Can't order more than the maximum quantity. ", quantity)

        return super().buy(quantity)
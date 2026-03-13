class Product:
    def __init__(self, name:str, price:float, quantity:int):
        if name == "":
            raise AttributeError("Product name cannot be empty")
        if price < 0:
            raise AttributeError("Product price cannot be negative")

        self.name = name
        self.price = price
        self.set_quantity(quantity)

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity:int):
        if (quantity < 0):
            raise AttributeError("Product quantity cannot be negative")

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
        self.set_quantity(self.get_quantity() - quantity)
        return float(self.price * quantity)

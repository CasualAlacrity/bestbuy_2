from promotions import Promotion, PercentDiscountPromotion, ThirdOneFreePromotion, SecondHalfPricePromotion


class Product:
    def __init__(self, name:str, price:float, quantity:int):
        if name == "":
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self._promotions:list[Promotion] = []
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity:int):
        if self.get_quantity() < 0:
            raise ValueError("Product quantity cannot be negative")

        self.quantity = quantity

        if self.get_quantity() > 0:
            self.activate()
        else:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def __str__(self)-> str:
        # "MacBook Air M2, Price: 1450, Quantity: 100"
        # I checked, and it seems that this function was not intended to return a value. Weird.
        return (f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if self.get_quantity() < quantity:
            raise ValueError("Not enough items in stock.")

        self.set_quantity(self.get_quantity() - quantity)

        final_price = self.price * quantity

        for promo in self._promotions:
            final_price = promo.apply_promotion(final_price, self.price, quantity)

        return round(final_price, 2)

    def set_promotion(self, promotion:Promotion):
        self._promotions.append(promotion)

class NonStockedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int = 0):
        super().__init__(name, price, quantity)

    def __str__(self)-> str:
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited"

    def set_quantity(self, quantity:int):
        self.quantity = 0
        self.activate()

    def buy(self, quantity) -> float:
        # I don't call super here because quantity checks caused issues
        final_price = self.price * quantity

        for promo in self._promotions:
            final_price = promo.apply_promotion(final_price, self.price, quantity)

        return round(final_price, 2)


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum:int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def __str__(self)-> str:
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, Maximum: {self.maximum} (Per Order)"

    def buy(self, quantity) -> float:
        if quantity > self.maximum:
            raise ValueError("Can't order more than the maximum quantity. ", quantity)

        return super().buy(quantity)
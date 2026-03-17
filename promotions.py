from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, promotion_title:str):
        self.__promotion_title = promotion_title

    @abstractmethod
    def apply_promotion(self, current_total:float, price:float, quantity:int) -> float:
        pass


class SecondHalfPricePromotion(Promotion):
    def __init__(self, promotion_title:str):
        super().__init__(promotion_title)

    def apply_promotion(self, current_total:float, price:float, quantity:int) -> float:
        pairs = quantity // 2
        discount = pairs * (price * 0.5)
        return current_total - discount

class ThirdOneFreePromotion(Promotion):
    def __init__(self, promotion_title:str):
        super().__init__(promotion_title)

    def apply_promotion(self, current_total:float, price:float, quantity:int) -> float:
        free_items = quantity // 3
        discount = free_items * price
        return current_total - discount


class PercentDiscountPromotion(Promotion):
    def __init__(self, promotion_title:str, percent:int):
        super().__init__(promotion_title)
        self._percent_discount = percent/100

    def apply_promotion(self, current_total:float, price:float, quantity:int) -> float:
        discount = current_total * self._percent_discount
        return current_total - discount
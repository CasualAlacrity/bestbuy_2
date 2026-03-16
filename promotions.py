class Promotion:
    def __init__(self, promotion_title:str):
        self.__promotion_title = promotion_title


class SecondHalfPricePromotion(Promotion):
    def __init__(self, promotion_title:str):
        super().__init__(promotion_title)

class ThirdOneFreePromotion(Promotion):
    def __init__(self, promotion_title:str):
        super().__init__(promotion_title)


class PercentDiscountPromotion(Promotion):
    def __init__(self, promotion_title:str, percent:int):
        super().__init__(promotion_title)
        self._percent_discount = percent

    @property
    def percent_discount(self)->int:
        return self._percent_discount
import pytest

import os

from promotions import Promotion, PercentDiscountPromotion, SecondHalfPricePromotion, ThirdOneFreePromotion

print(os.getcwd())

from product import Product


# Create Product Works
def test_create_product():
    product = Product("test", 100, 100)
    assert product.name == "test"
    assert product.price == 100


# Empty name error handling
def test_empty_name():
    product = None
    with pytest.raises(ValueError):
        product = Product("", 100, 100)


# Negative price error handling
def test_negative_price():
    product = None
    with pytest.raises(ValueError):
        product = Product("test", -100, 100)


# Negative quantity error handling
def test_negative_quantity():
    product = None
    with pytest.raises(ValueError):
        product = Product("test", 100, -100)


# Deactivates when quantity hits 0
def test_deactiveate_zero_quantity_buy():
    product = Product("test", 100, 1)
    product.buy(1)
    assert product.get_quantity() == 0


def test_deactiveate_zero_quantity_set():
    product = Product("test", 100, 1)
    product.set_quantity(0)
    assert product.get_quantity() == 0


# Purchasing decreases quantity and returns correct output
def test_purchase_decrease_quantity():
    product = Product("test", 100, 3)
    product.buy(1)
    assert product.get_quantity() == 2


# Purchasing larger quantities than exist error handled
def test_purchase_more_than_in_stock():
    product = Product("test", 100, 1)
    with pytest.raises(ValueError):
        product.buy(2)


# Test percent discount promo
def test_percent_off_promo():
    product = Product("test", 90, 2)
    promotion = PercentDiscountPromotion("30% off!", percent=30)
    product.set_promotion(promotion)
    price = product.buy(1)
    assert price == 63


# Test BOGO half off promo
def test_bogo_promotion():
    product = Product("test", 100, 2)
    promotion = SecondHalfPricePromotion("Second Half price!")
    product.set_promotion(promotion)
    price = product.buy(2)
    assert price == 150


def test_bogo_promotion_multi():
    product = Product("test", 100, 5)
    promotion = SecondHalfPricePromotion("Second Half price!")
    product.set_promotion(promotion)
    price = product.buy(5)
    assert price == 400


# Test "buy two, get one free" promo
def test_buy_2_get_1_promotion():
    product = Product("test", 100, 10)
    promotion = ThirdOneFreePromotion("Third One Free!")
    product.set_promotion(promotion)
    price = product.buy(7)
    assert price == 500


# Test Combo promos
def test_combo_promotion():
    product = Product("test", 100, 10)
    first_promotion = ThirdOneFreePromotion("Third One Free!")
    second_promotion = PercentDiscountPromotion("30% off!", percent=30)
    product.set_promotion(first_promotion)
    product.set_promotion(second_promotion)
    price = product.buy(3)
    assert price == 140

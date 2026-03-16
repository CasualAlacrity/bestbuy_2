import pytest

import os
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
import pytest

from products import Product

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
# Negative quantity error handling
# Deactivates when quantity hits 0
# Purchasing decreases quantity and returns correct output
# Purchasing larger quantities than exist error handled
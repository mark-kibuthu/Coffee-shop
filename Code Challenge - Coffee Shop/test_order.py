# tests/test_order.py

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_price_validation():
    customer = Customer("Bob")
    coffee = Coffee("Americano")
    with pytest.raises(ValueError):
        order = Order(customer, coffee, 0.5)

def test_order_relationship():
    customer = Customer("Eve")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 4.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

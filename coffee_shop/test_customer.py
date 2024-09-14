# tests/test_customer.py

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_create_order():
    customer = Customer("John")
    coffee = Coffee("Espresso")
    customer.create_order(coffee, 5.0)
    assert len(customer.orders()) == 1
    assert customer.orders()[0].price == 5.0
    assert coffee.orders()[0].customer == customer

def test_customer_name_validation():
    with pytest.raises(ValueError):
        customer = Customer("")

    with pytest.raises(ValueError):
        customer = Customer("This name is way too long for a customer")

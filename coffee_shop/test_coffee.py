import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        coffee = Coffee("a")

def test_coffee_average_price():
    coffee = Coffee("Latte")
    assert coffee.average_price() == 0

    customer = Customer("Alice")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 7.0)

    assert coffee.average_price() == 6.0

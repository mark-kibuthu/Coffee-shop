from customer import Customer
from coffee import Coffee

# customers and coffee
alice = Customer("Alice")
bob = Customer("Bob")

espresso = Coffee("Espresso")
latte = Coffee("Latte")

# Alice orders an espresso and a latte
alice.create_order(espresso, 3.5)
alice.create_order(latte, 4.5)

# Bob orders a latte
bob.create_order(latte, 4.0)

# Check Alice's orders
print(f"Alice's orders: {alice.orders()}")

# Check which coffees Alice ordered
print(f"Coffees Alice ordered: {alice.coffees()}")

# Check which customers ordered a latte
print(f"Customers who ordered a latte: {latte.customers()}")

# Check the number of orders and average price for latte
print(f"Number of orders for latte: {latte.num_orders()}")
print(f"Average price for latte: {latte.average_price()}")

# Find who spent the most on latte
print(f"Customer who spent the most on latte: {Customer.most_aficionado(latte)}")

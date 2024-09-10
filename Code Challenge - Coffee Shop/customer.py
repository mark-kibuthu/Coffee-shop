class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        """Returns all orders associated with the customer."""
        return self._orders

    def add_order(self, order):
        """Adds an order to the customer."""
        self._orders.append(order)

    def coffees(self):
        """Returns a list of unique Coffee objects the customer has ordered."""
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        """Creates an order and associates it with the customer and coffee."""
        from order import Order
        order = Order(self, coffee, price)
        self.add_order(order)
        coffee.add_order(order)

    @classmethod
    def most_aficionado(cls, coffee):
        """will return the customer who has spent the most on a particular coffee."""
        customer_spending = {}
        for order in coffee.orders():
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get, default=None)
    def __repr__(self):
        return f"Customer({self.name})"
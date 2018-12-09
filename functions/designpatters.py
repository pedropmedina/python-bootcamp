from collections import namedtuple

# Taken from Fluent Python

# Strategies:
# Family of interchangeable encapsulated algorithms. Strategy
# let the algorithm vary independently from clients that use it


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = f'<Order total: {self.total():.2f} due: {self.due():.2f}>'
        return fmt


# The strategies are plain functions. We'll pass functions as promotion arg
Customer = namedtuple('Customer', 'name fidelity')


def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * 0.05


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)


promos = [fidelity_promo, bulk_item_promo, large_order_promo]

joe = Customer('John Doe', 0)

cart = [
    LineItem('banana', 4, 0.5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0),
]

joe_order = Order(joe, cart, fidelity_promo)
print(joe_order)

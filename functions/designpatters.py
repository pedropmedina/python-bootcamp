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

# This functions will be use as a decorator
# By using this decorator we ensure that each new promo functions
# is added to the promos list without doing to much checking as
# every time a new function is decorated with promotions, promotions
# will run adding the decorated function to the list
def promotions(promo_fn):
    promos.append(promo_fn)
    return promo_fn


@promotions
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * 0.05


@promotions
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


@promotions
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


@promotions
def best(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)


promos = [fidelity, bulk_item, large_order]

joe = Customer('John Doe', 0)

cart = [
    LineItem('banana', 4, 0.5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0),
]

joe_order = Order(joe, cart, fidelity)
print(joe_order)

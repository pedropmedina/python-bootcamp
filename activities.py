def eat(food, is_healthy):
    ending = "and I don't care."
    if is_healthy:
        ending = "because it is healthy"
    return f"I'm eating {food}, {ending}"


def nap(num_hours):
    if num_hours > 2:
        return f"Ugh I overslept. I didn't mean to nap for {num_hours} hour."
    return "I'm feeling refreshed after my 1 hour nap"


def is_funny(person):
    if person is "tim":
        return False
    return True

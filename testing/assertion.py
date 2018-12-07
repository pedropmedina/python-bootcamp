def eat_junk(food):
    assert food in (
        "pizza",
        "ice cream",
        "candy",
        "fried butter",
    ), f"{food} is not junk food."
    return f"I am eating {food}"


food = input("What type of food are you eating? \n")
print(eat_junk(food))

# tuples are immutable as oposite of dicts and list
# tuples are also faster than lists
# We can nest tuples
# Also we can slice tuples with [:]
alphabet = ("a", "b", "c", "d", "e", "...")

alphabet[0]  # "a"

print(type(alphabet))

# tuples can be used as a property to a dic
dictionary = {
    ("Bianca", "Medina"): "CEO",
    ("Pedro", "Medina"): "CTO",
    ("Luca", "Medina"): "CFO",
}

print(dictionary[("Bianca", "Medina")])

# iterating over tuples is the same as list
for letter in alphabet:
    print(letter)

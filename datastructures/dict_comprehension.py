# list of tuples
students = [
    ('Pedro', 29),
    ('Bianca', 33),
    ('John', 28),
    ('Jane', 22),
    ('Johana', 21),
    ('Anne', 35),
    ('Annete', 36),
]

name_age = {name: age for name, age in students}
# output:
# {'Pedro': 29, 'Bianca': 33, 'John': 28, 'Jane': 22, 'Johana': 21, 'Anne': 35, 'Annete': 36}

descriptive_key = {f'{name}_age': age for name, age in name_age.items()}
# output
# {'Pedro_age': 29, 'Bianca_age': 33, 'John_age': 28, 'Jane_age': 22, 'Johana_age': 21, 'Anne_age': 35, 'Annete_age': 36}

string_1 = "ABC"
string_2 = "123"
new_dict = {string_1[i]: string_2[i] for i in range(0, len(string_1))}
print(new_dict)
# output:
# { "A": 1, "B": 2, "C": 3}

# Using a ternary operation for value
parity = {num: "even" if num % 2 == 0 else "odd" for num in range(0, 10)}
print(parity)
# output
# {0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd'}

# Ternanry operation for bot key and value
person = {"name": "Luca", "age": 4, "gender": "male"}
modified_person = {
    (k.upper() if k == "name" else k): (v.upper() if type(v) is not int else v)
    for k, v in person.items()
}
print(modified_person)

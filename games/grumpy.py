class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"YOU WANT {key}?, WELL IT AIN'T HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY")
        print("OK FINE...")
        super().__setitem__(key, value)


data = GrumpyDict({"first": "Jane", "city": "New York"})
print(data)

data["age"]
print(data)

data["city"] = "San Francisco"
print(data)

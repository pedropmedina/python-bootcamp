from csv import DictReader, reader, writer

# with open("csvdata.csv") as file:
#     csv_reader = reader(file)  # returns an iterator
#     for each in csv_reader:
#         print(f"{each[0]} -> {each[-1]}")

# with open("csvdata.csv") as file:
#     csv_reader = DictReader(file)  # returns an OrderedDict
#     for each in csv_reader:
#         print(each["first_name"])

with open("csvdata.csv") as file:
    csv_reader = reader(file)
    short_list = [[entry.upper() for entry in each] for each in csv_reader][:3]


with open("new_csvdata.csv", "w") as file:
    csv_writer = writer(file)
    for each in short_list:
        csv_writer.writerow(each)

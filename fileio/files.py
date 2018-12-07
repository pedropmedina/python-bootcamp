# file = open("story.txt")
# print(file.read())

# open() opens I/O
# read() reads entire file
# closed Bool that checks I/O
# close() closes I/O
# seek(num) goes back to the given line
# readline() returns given line
# readlines() retuens list of each line

# with open("story.txt") as f:
#     data = f.read
# with triggers __enter__ and __exit__ wich automatically
# opens and closed the I/O operation

# overwrites everything in file or creates new file if none exists
with open("story.txt", "w") as f:
    f.write("Hello there my friends \n")
    f.write("from earth, greetings and goodbye \n")

# appends to existing file, or creates new file if none exists
with open("story.txt", "a") as f1:
    f1.write("This new line gets appended to the story.txt file")

# r+ lets us move the cursor around. By default it starts at 0.
# It overwrites the content in file instead of shifting it
with open("story.txt", "r+") as f2:
    f2.write("BEFORE ANYTING ELSE IN THIS FILE")

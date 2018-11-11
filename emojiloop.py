# Solution 1
num = 1
while num < 11:
    print(' 😄 ' * num)
    num += 1

# Solution 2
for num in range(1, 11):
    print(' 😄 ' * num)

# Solution 3
for num in range(1, 11):
    emoji = ''
    count = 1
    while count <= num:
        emoji += ' 😄 '
        count += 1
    print(emoji)

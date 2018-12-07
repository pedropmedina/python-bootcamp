print('How many kilometers did you cycle today?')
kms = float(input())  # input always returns a str
miles = round(kms / 1.6934, 2)
print(f'Ok you said {miles} miles.')

# age = input('How are you?\n')

# if age and not(age != str):
#     int_age = int(age)

#     if int_age >= 10 and int_age < 21:
#         print('You can enter, but need a wristband!')
#     elif int_age >= 21:
#         print('You are good to enter and you can drink')
#     else:
#         print('You can\'t come in.😟')
# else:
#     print('Make sure to provide age')

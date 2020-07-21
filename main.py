import random

chars = '!@#$%*1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number_passwords = int(input("Number of passwords? \n"))
password_length = int(input("Number of characters? \n"))

for p in range(number_passwords):
    password = ''
    for c in range(password_length):
        password += random.choice(chars)
    print(password)
input("Press ENTER to exit")

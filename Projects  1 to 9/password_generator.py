
import random

print("Welcome to the Password Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

number_of_passwords = int(input("How many passwords would you like to generate? "))
length_of_password = int(input("How long would you like your passwords to be? "))

print("\nHere are your passwords:")
for pwd in range(number_of_passwords):
    passwords = ''
    for c in range(length_of_password):
        passwords += random.choice(chars)
    print(passwords)
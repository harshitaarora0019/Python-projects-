import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_chars = "!@#$%^&*()"

all_chars = letters + digits + special_chars

length = int(input("Enter password length: "))
password = ""

for i in range(length):
    password += random.choice(all_chars)

print("Generated password:", password)


import random

chars = "abcdefghijklmnopqrstvwxyz1234567890"
password = ""
for c in range(10):
    password += random.choice(chars)
print(password)

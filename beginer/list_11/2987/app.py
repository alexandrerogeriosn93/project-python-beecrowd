from string import ascii_uppercase

alphabet = dict()

for index, value in enumerate(ascii_uppercase):
    alphabet[value] = index + 1

l = input().upper()

print(alphabet[l])

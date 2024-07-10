from string import ascii_uppercase

alphabet = dict()

for index, value in enumerate(ascii_uppercase, start=1):
    alphabet[value] = index

l = input().upper()

print(alphabet[l])

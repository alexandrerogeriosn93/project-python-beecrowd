def validate(n):
    return n < 0 or n > 10

x = float(input())

while validate(x):
    print("nota invalida")
    x = float(input())

y = float(input())

while validate(y):
    print("nota invalida")
    y = float(input())

average = (x + y) / 2

print(f"media = {average:.2f}")

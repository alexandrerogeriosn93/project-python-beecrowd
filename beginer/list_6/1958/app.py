from decimal import Decimal

x = input()

if Decimal(x) >= 0 and x[0] != "-":
    print("+", end="")

print("%.4E" % Decimal(x))

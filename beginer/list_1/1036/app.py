from math import pow, sqrt


def calc_delta(a, b, c):
    return pow(b, 2) - 4 * a * c


def calc_x1_and_x2(a, b, delta):
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    return x1, x2


a, b, c = map(float, input().split())

try:
    delta = calc_delta(a, b, c)
    x1, x2 = calc_x1_and_x2(a, b, delta)

    print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")
except ZeroDivisionError:
    print("Impossivel calcular")
except ValueError:
    print("Impossivel calcular")

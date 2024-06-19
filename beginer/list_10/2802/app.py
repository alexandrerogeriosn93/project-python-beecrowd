from math import pow

n = int(input())
n = int(((n / 24) * (pow(n, 3) - 6 * pow(n, 2) + 23 * n - 18)) + 1)

print(n)

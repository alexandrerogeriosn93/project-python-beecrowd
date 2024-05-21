vet_fibonacci = [0 for _ in range(61)]
vet_fibonacci[0] = 0
vet_fibonacci[1] = 1

for i in range(2, 61):
    vet_fibonacci[i] = vet_fibonacci[i - 2] + vet_fibonacci[i - 1]

n = int(input())

for i in range(n):
    x = int(input())
    print(f"Fib({x}) = {vet_fibonacci[x]}")

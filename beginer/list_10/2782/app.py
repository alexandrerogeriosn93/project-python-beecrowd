def validate(vet, i):
    return vet[i] - vet[i - 1] != vet[i - 1] - vet[i - 2]


n = int(input())
sequence = list(map(int, input().split()))
stairs = 1

for i in range(2, n):
    if validate(sequence, i):
        stairs += 1

print(stairs)

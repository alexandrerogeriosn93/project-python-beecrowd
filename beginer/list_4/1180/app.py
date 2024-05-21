n = int(input())
vet = list(map(int, input().split()))

min_value = min(vet)
min_position = vet.index(min_value)

print(f"Menor valor: {min_value}\nPosicao: {min_position}")

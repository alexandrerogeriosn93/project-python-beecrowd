t = int(input())
vet = [] 

for i in range(1000):
    j = 0
    while j < t:
        vet.append(j)
        j = j + 1
    print(f"N[{i}] = {vet[i]}")

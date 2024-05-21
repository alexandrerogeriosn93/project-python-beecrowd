vet_even, vet_odd = [], []
even, odd = 0, 0

for i in range(15):
    x = int(input())

    if x % 2 == 0:
        vet_even.append(x)
        even += 1
    else:
        vet_odd.append(x)
        odd += 1

    if even > 4:
        for j in range(5):
            print(f"par[{j}] = {vet_even[j]}")
        vet_even = []
        even = 0

    if odd > 4:
        for j in range(5):
            print(f"impar[{j}] = {vet_odd[j]}")
        vet_odd = []
        odd = 0

if odd > 0:
    for i in range(odd):
        print(f"impar[{i}] = {vet_odd[i]}")

if even > 0:
    for i in range(even):
        print(f"par[{i}] = {vet_even[i]}")

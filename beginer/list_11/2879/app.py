n = int(input())
vet = []

for _ in range(n):
    num = int(input())
    if num != 1:
        vet.append(num)

print(len(vet))

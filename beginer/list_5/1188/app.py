mat = [[0 for _ in range(12)] for _ in range(12)]
option = input().upper()
sum_elements = counter = 0
init = 5
limit = 7

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())

for i in range(7, 12):
    for j in range(init, limit):
        sum_elements += mat[i][j]
        counter += 1
    init -= 1
    limit += 1

print(f"{sum_elements:.1f}" if option == "S" else f"{(sum_elements / counter):.1f}")

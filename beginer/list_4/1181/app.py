mat = [[0 for _ in range(12)] for _ in range(12)]
line = int(input())
option = input().upper()
sum_line = 0

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())

for i in range(12):
    sum_line += mat[line][i]

response = f"{sum_line:.1f}" if option == "S" else f"{(sum_line/12):.1f}"
print(response)

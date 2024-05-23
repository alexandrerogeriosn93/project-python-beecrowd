mat = [[0 for _ in range(12)] for _ in range(12)]
column = int(input())
option = input().upper()
sum_column = 0

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())

for i in range(12):
    sum_column += mat[i][column]

response = f"{sum_column:.1f}" if option == "S" else f"{(sum_column/12):.1f}"
print(response)

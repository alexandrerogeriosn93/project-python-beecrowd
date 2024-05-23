mat = [[0 for _ in range(12)] for _ in range(12)]
option = input().upper()
sum_elements = 0
counter = 0
column = 11

for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())

for i in range(1, 11):
    for j in range(column, 12):
        sum_elements += mat[i][j]
        counter += 1

    if i < 5:
        column -= 1
    
    if i > 5:
        column += 1

response = f"{sum_elements:.1f}" if option == "S" else f"{(sum_elements/counter):.1f}"
print(response)

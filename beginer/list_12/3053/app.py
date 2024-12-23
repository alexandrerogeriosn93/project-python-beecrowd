def change_values(values, i, j):
    values[i], values[j] = values[j], values[i]


n = int(input())

initial_position = ord(input()) - 65
abc = [0, 0, 0]
abc[initial_position] = 1

for _ in range(n):
    op = int(input())

    if op == 1:
        change_values(abc, 0, 1)
    elif op == 2:
        change_values(abc, 2, 1)
    elif op == 3:
        change_values(abc, 0, 2)

final_position = chr(abc.index(1) + 65)
print(f"{final_position}")

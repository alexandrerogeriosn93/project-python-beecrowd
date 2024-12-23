import sys

input = sys.stdin.read

data = input().strip().split("\n")
n = int(data[0])

house_bought = leftover_house = work_bought = leftover_work = 0

for i in range(1, n + 1):
    go_work, go_home = data[i].split()

    if go_work == "chuva" and leftover_house == 0:
        house_bought += 1
        leftover_work += 1
    elif go_work == "chuva" and leftover_house > 0:
        leftover_work += 1
        leftover_house -= 1

    if go_home == "chuva" and leftover_work == 0:
        work_bought += 1
        leftover_house += 1
    elif go_home == "chuva" and leftover_work > 0:
        leftover_house += 1
        leftover_work -= 1

print(house_bought, work_bought)

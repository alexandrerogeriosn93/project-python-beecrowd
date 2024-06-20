def is_odd(value):
    return value % 2 == 1

n = int(input())

for _ in range(n):
    m = int(input())
    list_mi = sorted(list(map(int, input().split())), reverse=True)
    list_odd = []

    while True:
        flag = False

        for i in list_mi:
            if is_odd(i):
                list_odd.append(i)
                list_mi.remove(i)
                list_mi.reverse()
                flag = True
                break

        if flag == False:
            break

    print(*list_odd)

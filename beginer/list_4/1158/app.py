n = int(input())

for i in range(0, n):
    x, y = map(int, input().split())
    response, counter = 0, 0

    while counter < y:
        if x % 2 != 0:
            response += x
            counter += 1
        x += 1

    print(response)

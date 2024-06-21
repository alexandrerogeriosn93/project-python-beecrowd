from math import ceil

while True:
    try:
        n = int(input())
        answer = ceil(n / 100)
        print(answer)
    except EOFError:
        break

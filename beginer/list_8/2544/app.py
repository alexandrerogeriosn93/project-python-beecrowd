from math import log

while True:
    try:
        n = int(input())
        print(int(log(n, 2)))
    except EOFError:
        break

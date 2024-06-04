while True:
    try:
        n = int(input())
        votes = sum(list(map(int, input().split())))
        impeachment = 2 * n / 3
        res = "impeachment" if votes >= impeachment else "acusacao arquivada"
        print(res)
    except EOFError:
        break

while True:
    try:
        n = int(input())
        votes = sum(list(map(int, input().split())))
        impeachment = 2 * n / 3
        print("impeachment" if votes >= impeachment else "acusacao arquivada")
    except EOFError:
        break

# Reference
# https://github.com/xTecna/solucoes-da-beecrowd/blob/main/problemas/iniciante/2542/README.md

while True:
    try:
        n = int(input())
        marcos, leonardo = map(int, input().split())
        cards_marcos = [list(map(int, input().split())) for _ in range(marcos)]
        cards_leonardo = [list(map(int, input().split())) for _ in range(leonardo)]
        cm, cl = map(int, input().split())
        a = int(input())

        marcos_card = cards_marcos[cm - 1][a - 1]
        leonardo_card = cards_leonardo[cl - 1][a - 1]

        if marcos_card > leonardo_card:
            print("Marcos")
        elif leonardo_card > marcos_card:
            print("Leonardo")
        else:
            print("Empate")
    except EOFError:
        break

# Reference
# https://github.com/xTecna/solucoes-da-beecrowd/blob/main/problemas/iniciante/2520/README.md

def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

while True:
    try:
        N, M = map(int, input().split())
        x1, y1, x2, y2 = 0, 0, 0, 0

        for i, line in enumerate([list(map(int, input().split())) for _ in range(N)]):
            for j, element in enumerate(line):
                if element == 1:
                    x1, y1 = i, j
                elif element == 2:
                    x2, y2 = i, j

        print(calc_distance(x1, y1, x2, y2))
    except EOFError:
        break

def return_quadrant(x, y):
    res = ""

    if x == 0.0 and y == 0.0:
        res = "Origem"
    elif x == 0.0 and y != 0.0:
        res = "Eixo Y"
    elif x != 0.0 and y == 0.0:
        res = "Eixo X"
    elif x > 0.0 and y > 0.0:
        res = "Q1"
    elif x < 0.0 and y > 0.0:
        res = "Q2"
    elif x < 0.0 and y < 0.0:
        res = "Q3"
    else:
        res = "Q4"

    return res

x ,y = map(float, input().split())

print(return_quadrant(x, y))

while True:
    try:
        v = float(input())
        d = float(input())
        r = d / 2
        area = 3.14 * (r * r)
        height = v / area

        print(f"ALTURA = {height:.2f}\nAREA = {area:.2f}")
    except EOFError:
        break

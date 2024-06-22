b, g = int(input()), int(input())
res = g // 2

print("Amelia tem todas bolinhas!" if res <= b or b >= g else f"Faltam {res-b} bolinha(s)")

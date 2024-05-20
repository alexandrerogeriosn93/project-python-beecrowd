n = int(input())

for i in range(n):
    try:
        x, y = map(int, input().split())
        print(f"{(x / y):.1f}")
    except ZeroDivisionError:
        print("divisao impossivel")

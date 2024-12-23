def check_condition(a, b, c):
    return a + b == c or a + c == b or b + c == a or a == b or a == c or b == c


a, b, c = map(int, input().split())

print("S" if check_condition(a, b, c) else "N")

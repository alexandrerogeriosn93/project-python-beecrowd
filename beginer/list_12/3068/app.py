def validate_entry(x1, x2, y1, y2):
    return x1 == x2 == y1 == y2 == 0

def validate_interview(x1, x, x2, y1, y, y2):
    return x1 <= x <= x2 and y2 <= y <= y1

tests = 0

while True:
    tests += 1
    x1, y1, x2, y2 = map(int, input().split())

    if validate_entry(x1, x2, y1 ,y2):
        break

    n = int(input())
    total = 0

    for _ in range(n):
        x, y = map(int, input().split())

        if validate_interview(x1, x, x2, y1, y, y2):
            total += 1

    print(f"Teste {tests}\n{total}")

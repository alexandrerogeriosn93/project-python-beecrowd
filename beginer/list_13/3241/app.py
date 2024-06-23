n = int(input())

for _ in range(n):
    entry = input()

    if "+" in entry:
        x, y = map(int, entry.split("+"))
        print(x + y)
    else:
        print("skipped")

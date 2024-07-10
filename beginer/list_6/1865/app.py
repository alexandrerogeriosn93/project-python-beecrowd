n = int(input())

for i in range(n):
    name, force = map(str, input().split())
    force = int(force)

    print("Y" if name == "Thor" else "N")

n = int(input())

for i in range(n):
    t = int(input())
    response = t - 2015

    print(f"{response * -1} D.C.") if response < 0 else print(f"{response + 1} A.C.")

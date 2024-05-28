n = int(input())

for i in range(n):
    h, m, o = map(int, input().split())
    response = "abriu" if o == 1 else "fechou"

    print(f"{str(h).zfill(2)}:{str(m).zfill(2)} - A porta {response}!")

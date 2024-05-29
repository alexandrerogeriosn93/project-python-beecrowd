while (t := int(input())) != 0:
    for i in range(1, t + 1):
        n = int(input())

        print(f"{(n * 2) - 1}") if n % 2 != 0 else print(f"{(n * 2) - 2}")

while (n := int(input())) != 0:
    for i in range(1, n + 1):
        print(i, end=[" ", "\n"][i == n])

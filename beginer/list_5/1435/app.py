while (n := int(input())) > 0:
    mat = [[0 for _ in range(n)] for _ in range(n)]
    min_value = 0
    max_value = n
    counter = 0

    limit = n // 2 if n % 2 == 0 else 1 + n // 2

    for k in range(0, limit):
        counter += 1
        for i in range(min_value, max_value):
            for j in range(min_value, max_value):
                mat[i][j] = counter
        min_value += 1
        max_value -= 1

    for i in range(n):
        text = ""
        for j in range(n):
            text += " %3d" % mat[i][j]
        print(text[1:])
    print("")

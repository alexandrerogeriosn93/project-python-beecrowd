while (x := int(input())) != 0:
    response = 0

    for i in range(x, x + 10):
        if i % 2 == 0:
            response += i

    print(response)

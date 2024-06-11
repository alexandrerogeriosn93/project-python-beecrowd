while True:
    try:
        entry = []

        for _ in range(10):
            entry.append(input())

        print(f"{entry[2]}\n{entry[6]}\n{entry[8]}")
    except EOFError:
        break

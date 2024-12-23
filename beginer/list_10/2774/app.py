while True:
    try:
        hm = map(int, input().split())
        values = list(map(float, input().split()))
        average = sum(values) / len(values)
        answer = 0

        for value in values:
            answer += (value - average) ** 2

        answer = (answer / (len(values) - 1)) ** (1 / 2)
        print(f"{answer:.5f}")
    except EOFError:
        break

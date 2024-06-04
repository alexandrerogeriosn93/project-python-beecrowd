while True:
    try:
        text = input().strip()
        n = int(input())
        indexes = list(map(int, input().split()))
        response = "".join(text[index - 1] for index in indexes)

        print(response)
    except EOFError:
        break

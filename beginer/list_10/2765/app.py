while True:
    try:
        entry = input().split(",")

        for text in entry:
            print(text)
    except EOFError:
        break

while True:
    try:
        n = int(input())

        for _ in range(n):
            text = input()
            print("I am Toorg!")
    except EOFError:
        break

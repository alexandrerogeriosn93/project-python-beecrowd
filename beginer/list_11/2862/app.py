while True:
    try:
        n = int(input())

        for _ in range(n):
            print("Mais de 8000!" if int(input()) > 8000 else "Inseto!")
    except EOFError:
        break

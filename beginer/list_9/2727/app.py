def decrypt(text):
    print(chr(ord("a") + 3 * (len(text) - 1) + len(text[0]) - 1))


while True:
    try:
        n = int(input())

        for _ in range(n):
            text = input().split()
            decrypt(text)
    except EOFError:
        break

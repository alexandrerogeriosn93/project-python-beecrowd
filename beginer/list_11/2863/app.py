while True:
    try:
        n = int(input())
        vet = []

        for _ in range(n):
            vet.append(float(input()))

        print(min(vet))
    except EOFError:
        break

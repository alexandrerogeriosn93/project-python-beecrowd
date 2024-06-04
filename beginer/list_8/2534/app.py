while True:
    try:
        n, q = map(int, input().split())
        vet_p = []

        for _ in range(n):
            vet_p.append(int(input()))

        vet_p.sort(reverse=True)

        for _ in range(q):
            x = int(input())
            print(vet_p[x - 1])
    except EOFError:
        break

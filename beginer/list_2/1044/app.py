a, b = map(int, input().split())

if a < b:
    a, b = b, a

print("Sao Multiplos" if a % b  == 0 else "Nao sao Multiplos")

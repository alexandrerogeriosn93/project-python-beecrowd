bird = {
    "esquerda": "ingles",
    "direita": "frances",
    "nenhuma": "portugues",
    "as duas": "caiu"
}

while True:
    try:
        n = input()
        print(bird[n])
    except EOFError:
        break

p, j1, j2, r, a = map(int, input().split())

if r == 1:
    if a == 1:
        print("Jogador 2 ganha!")
    else:
        print("Jogador 1 ganha!")
else:
    if a == 1:
        print("Jogador 1 ganha!")
    else:
        if (j1 + j2) % 2 == 0:
            if p == 0:
                print("Jogador 2 ganha!")
            else:
                print("Jogador 1 ganha!")
        else:
            if p == 0:
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")

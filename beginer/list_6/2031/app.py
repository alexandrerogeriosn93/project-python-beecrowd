n = int(input())

for i in range(n):
    player_1 = input().strip().lower()
    player_2 = input().strip().lower()

    if player_1 == "ataque":
        if player_2 == "ataque":
            print("Aniquilacao mutua")
        else:
            print("Jogador 1 venceu")
    elif player_1 == "papel":
        if player_2 == "ataque" or player_2 == "pedra":
            print("Jogador 2 venceu")
        else:
            print("Ambos venceram")
    elif player_1 == "pedra":
        if player_2 == "papel":
            print("Jogador 1 venceu")
        if player_2 == "ataque":
            print("Jogador 2 venceu")
        elif player_2 == "pedra":
            print("Sem ganhador")

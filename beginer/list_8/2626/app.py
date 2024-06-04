def get_winner(first_move, second_move):
    moves = (("pedra", "tesoura"), ("tesoura", "papel"), ("papel", "pedra"))
    return (first_move, second_move) in moves

messages = {
    ("pedra", "tesoura"): "Os atributos dos monstros vao ser inteligencia, sabedoria...",
    ("tesoura", "papel"): "Iron Maiden's gonna get you, no matter how far!",
    ("papel", "pedra"): "Urano perdeu algo muito precioso...",
}

while True:
    try:
        dodo, leo, pepper = input().strip().split(' ')

        if (get_winner(dodo, leo) and get_winner(dodo, pepper)):
            print(messages[("pedra", "tesoura")])
        elif (get_winner(leo, dodo) and get_winner(leo, pepper)):
            print(messages[("tesoura", "papel")])
        elif (get_winner(pepper, dodo) and get_winner(pepper, leo)):
            print(messages[("papel", "pedra")])
        else:
            print("Putz vei, o Leo ta demorando muito pra jogar...")
    except EOFError:
        break

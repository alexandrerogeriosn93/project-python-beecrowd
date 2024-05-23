def show_message(i, message):
    print(f"Caso #{i}: {message}")

n = int(input())

for i in range(n):
    sheldon, raj = input().split()

    if sheldon == raj:
        show_message((i + 1), "De novo!")
    elif sheldon == "Spock" and raj == "pedra":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "lagarto" and raj == "Spock":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "tesoura" and raj == "lagarto":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "papel" and raj == "Spock":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "tesoura" and raj == "papel":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "papel" and raj == "pedra":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "lagarto" and raj == "papel":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "pedra" and raj == "lagarto":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "Spock" and raj == "tesoura":
        show_message((i + 1), "Bazinga!")
    elif sheldon == "pedra" and raj == "tesoura":
        show_message((i + 1), "Bazinga!")
    else:
        show_message((i + 1), "Raj trapaceou!")

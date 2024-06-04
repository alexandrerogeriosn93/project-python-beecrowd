# Reference
# https://github.com/xTecna/solucoes-da-beecrowd/blob/main/problemas/iniciante/2502/README.md

def create_dictionary(first_cipher, second_cipher):
    translate_dictionary = {}

    for c1, c2 in zip(first_cipher, second_cipher):
        translate_dictionary[c1] = c2
        translate_dictionary[c1.lower()] = c2.lower()
        translate_dictionary[c2] = c1
        translate_dictionary[c2.lower()] = c1.lower()

    return translate_dictionary

def decripty(phrase, translate):
    for letter in phrase:
        print(translate.get(letter, letter), end="")
    print("")

while True:
    try:
        C, N = map(int, input().strip().split())
        
        first_cipher = input()
        second_cipher = input()

        translate = create_dictionary(first_cipher, second_cipher)

        for _ in range(N):
            phrase = input()
            decripty(phrase, translate)
        print("")
    except EOFError:
        break

while True:
    try:
        m = int(input())
        m %= 360

        if m < 90:
            print("Bom Dia!!")
        elif m < 180:
            print("Boa Tarde!!")
        elif m < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")
    except EOFError:
        break

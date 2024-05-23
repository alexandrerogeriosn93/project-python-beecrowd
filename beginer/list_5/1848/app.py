for _ in range(3):
    response = 0

    while True:
        crow = input()

        if crow != "caw caw":
            crow = crow.replace("-", "0")
            crow = crow.replace("*", "1")
            crow = int(crow, 2)
            response += crow
        else:
            print(response)
            break

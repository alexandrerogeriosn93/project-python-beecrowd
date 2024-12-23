cases = 1
counter = position = flag = 0

while True:
    try:
        counter = 0
        n1 = input()
        n2 = input()
        print("Caso #{}:".format(cases))

        for i in range(len(n2)):
            if n1[0] == n2[i]:
                flag = 0

                for j in range(len(n1)):
                    if i + j >= len(n2):
                        break

                    if n1[j] == n2[i + j]:
                        flag += 1

                if flag == len(n1):
                    counter += 1
                    position = i + 1

        if counter == 0:
            print("Nao existe subsequencia")
        else:
            print("Qtd.Subsequencias: {}".format(counter))
            print("Pos: {}".format(position))

        print("")
        cases += 1
    except EOFError:
        break

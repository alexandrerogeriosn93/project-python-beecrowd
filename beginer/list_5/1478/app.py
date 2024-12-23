while (n := int(input())) > 0:
    mat = []

    for i in range(1, (n + 1)):
        mat_aux = []
        counter = i
        for j in range(n):
            mat_aux.append(abs(counter))
            counter = counter - 3 if counter == 1 else counter - 1
        mat.append(mat_aux)

    for i in range(n):
        text = ""
        for j in range(n):
            text += " %3d" % mat[i][j]
        print(text[1:])
    print("")

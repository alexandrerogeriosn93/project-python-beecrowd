a, b, c = sorted(map(int, input().split()))
type_triangle = ""

if a + b <= c:
    print("Invalido")
else:
    if a == b == c:
        type_triangle = "Valido-Equilatero"
    elif a == b or b == c:
        type_triangle = "Valido-Isoceles"
    else:
        type_triangle = "Valido-Escaleno"
    
    rectangle = "S" if a ** 2 + b ** 2 == c ** 2 else "N"
    
    print(f"{type_triangle}\nRetangulo: {rectangle}")

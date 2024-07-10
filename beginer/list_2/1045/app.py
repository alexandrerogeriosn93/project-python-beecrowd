from math import pow

values = list(map(float, input().split()))

a, b, c = sorted(values, reverse=True)
d = pow(a, 2)
e = pow(b, 2) + pow(c, 2)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if d == e:
        print("TRIANGULO RETANGULO")
    
    if d > e:
        print("TRIANGULO OBTUSANGULO")
    
    if d < e:
        print("TRIANGULO ACUTANGULO")
    
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")

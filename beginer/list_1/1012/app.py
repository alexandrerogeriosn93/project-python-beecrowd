from math import pow

A, B, C = map(float, input().split())

triangle = A * C / 2
circle = 3.14159 * pow(C, 2)
trapeze = (A + B) * C / 2
square = pow(B, 2)
rectangle = A * B

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapeze:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")

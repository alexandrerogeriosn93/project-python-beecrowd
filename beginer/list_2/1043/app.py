def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)

def calc_area(a, b, c):
    return ((a + b) * c) / 2 

def calc_perimeter(a, b, c):
    return a + b + c

a, b, c = map(float, input().split())

res =  f"Perimetro = {calc_perimeter(a, b, c):.1f}" if is_triangle(a, b, c) else f"Area = {calc_area(a, b, c):.1f}"

print(res)

h, e, a, o, w, x = map(int, input().split())

ex1 = h + e + a
ex2 = o + w

if ex1 <= ex2:
    ex1 += x

print("Middle-earth is safe." if ex1 >= ex2 else "Sauron has returned.")

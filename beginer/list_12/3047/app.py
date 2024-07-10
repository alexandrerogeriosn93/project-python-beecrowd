m = int(input())
a = int(input())
b = int(input())

max_age = m - a - b

if a < max_age > b:
    print(max_age)
elif a > b and a > max_age:
    print(a)
else:
    print(b)

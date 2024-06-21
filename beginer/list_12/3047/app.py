m = int(input())
a = int(input())
b = int(input())

max_age = m - a - b

if max_age > a and max_age > b:
    print(max_age)
elif a > b and a > max_age:
    print(a)
else:
    print(b)

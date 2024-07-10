def is_null(num):
    return num == 0

def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

n = int(input())

for i in range(n):
    num = int(input())

    if is_null(num):
        print("NULL")
    else:
        print("EVEN POSITIVE" if is_even(num) else "ODD POSITIVE") if is_positive(num) else print("EVEN NEGATIVE" if is_even(num) else "ODD NEGATIVE")

l = int(input())
c = int(input())

first_type = (l * c) + ((l - 1) * (c - 1))
second_type = ((l - 1) * 2) + ((c - 1) * 2)

print(f"{first_type}\n{second_type}")

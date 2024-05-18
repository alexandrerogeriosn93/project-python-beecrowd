a, b, c = [int(x) for x in input().split()]
list_a = []

list_a.append(a)
list_a.append(b)
list_a.append(c)

ordered_list = sorted(list_a)

for i in ordered_list:
    print(i)

print()

for i in list_a:
    print(i)

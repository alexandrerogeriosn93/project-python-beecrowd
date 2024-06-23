h, z, l = map(int, input().split())

ages = [h, z, l]
ages.sort()

if ages[1] == h:
    print("huguinho")
elif ages[1] == z:
    print("zezinho")
else:
    print("luisinho")

n = int(input())
hobbit = human = elf = mage = dwarf = 0

for _ in range(n):
    name, breed = input().split()

    match breed:
        case "A":
            dwarf += 1
        case "E":
            elf += 1
        case "H":
            human += 1
        case "M":
            mage += 1
        case "X":
            hobbit += 1

print(f"{hobbit} Hobbit(s)")
print(f"{human} Humano(s)")
print(f"{elf} Elfo(s)")
print(f"{dwarf} Anao(oes)")
print(f"{mage} Mago(s)")

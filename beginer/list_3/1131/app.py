grenais, draw = 0, 0
victories_gremio, victories_inter = 0, 0
option = 0

while option != 2:
    inter, gremio = map(int, input().split())

    if inter == gremio:
        draw += 1
    elif inter > gremio:
        victories_inter += 1
    else:
        victories_gremio += 1

    grenais += 1

    option = int(input("Novo grenal (1-sim 2-nao)\n"))

print(f"{grenais} grenais")
print(f"Inter:{victories_inter}")
print(f"Gremio:{victories_gremio}")
print(f"Empates:{draw}")

if draw > victories_gremio and draw > victories_inter:
    print("Nao houve vencedor")
elif victories_inter > victories_gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")

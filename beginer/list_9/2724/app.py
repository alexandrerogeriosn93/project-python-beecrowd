n = int(input())

for i in range(n):
    if i > 0:
        print()

    t = int(input())
    hazardous = []

    for _ in range(t):
        hazardous.append(input().strip())

    u = int(input())

    for _ in range(u):
        formula = input().strip()
        dangerous = False

        for element in hazardous:
            pos = formula.find(element)

            while pos != -1:
                ahead = pos + len(element)

                if ahead < len(formula):
                    next_char = formula[ahead - 1]
                    next_next_char = formula[ahead]

                    if (
                        (next_char.isdigit() and not next_next_char.isdigit())
                        or (next_char.isupper() and next_next_char.isupper())
                        or (next_char.islower() and next_next_char.isupper())
                    ):
                        dangerous = True
                        break
                else:
                    dangerous = True
                    break

                pos = formula.find(element, pos + 1)

            if dangerous:
                break

        print("Abortar" if dangerous else "Prossiga")

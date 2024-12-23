import sys


def validate(x, xi, y, yi):
    return xi <= x and yi <= y or xi <= y and yi <= x


input = sys.stdin.read().strip().split()

index = 0
results = []

while index < len(input):
    try:
        x = int(input[index])
        y = int(input[index + 1])
        m = int(input[index + 2])
        index += 3

        for _ in range(m):
            xi = int(input[index])
            yi = int(input[index + 1])
            index += 2

            results.append("Sim") if validate(x, xi, y, yi) else results.append("Nao")

    except ValueError:
        break

sys.stdout.write("\n".join(results) + "\n")

def len_sequence_numbers(n):
    total = 1

    for i in range(1, n + 1):
        total += i

    return total

def generate_sequence(n):
    vet_sequence = [0]

    for i in range(1, n + 1):
        vet_sequence.extend([i] * i)

    return vet_sequence

cases = 1

while True:
    try:
        n = int(input())
        quantity = len_sequence_numbers(n)
        sequence = generate_sequence(n)
        numbers = "numeros" if quantity != 1 else "numero"

        print(f"Caso {cases}: {quantity} {numbers}")
        print(" ".join(map(str, sequence)))
        print()

        cases += 1
    except EOFError:
        break

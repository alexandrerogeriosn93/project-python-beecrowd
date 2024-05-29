# Reference
# https://github.com/whitesimian/URI-Online-Judge/blob/master/Codes/2493.cpp

while True:
    try:
        t = int(input())
        vet = []
        names = set()

        for _ in range(t):
            text = input().split()
            aux = int(text[0])
            numbers = [int(x) for x in text[1].split("=")]
            vet.append([aux] + numbers)

        for _ in range(t):
            name, position, operation = input().split()
            position = int(position) - 1
            first, second, third = vet[position]

            match operation:
                case "+":
                    if first + second != third:
                        names.add(name)
                case "-":
                    if first - second != third:
                        names.add(name)
                case "*":
                    if first * second != third:
                        names.add(name)
                case "I":
                    if first + second == third or first - second == third or first * second == third:
                        names.add(name)

        if len(names) == 0:
            print("You Shall All Pass!")
        elif len(names) == t:
            print("None Shall Pass!")
        else:
            print(*(sorted(names)))
    except EOFError:
        break

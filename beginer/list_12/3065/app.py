tests = 0

while (m := int(input())) != 0:
    tests += 1
    total = 0

    operation = input().strip()    
    operator = "+"
    operation = operation.replace(" ", "")
    
    i = 0
    n = len(operation)

    while i < n:
        j = i

        while j < n and operation[j] not in "+-":
            j += 1

        number_str = operation[i:j]
        number = int(number_str)

        match operator:
            case "+":
                total += number
            case "-":
                total -= number

        i = j

        if i < n:
            operator = operation[i]
            i += 1

    print(f"Teste {tests}\n{total}\n")

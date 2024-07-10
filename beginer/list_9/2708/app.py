entry = input().split()
jeep = peolpe = 0

while entry[0] != "ABEND":
    match entry[0]:
        case "SALIDA":
            peolpe += int(entry[1])
            jeep += 1
        case "VUELTA":
            peolpe -= int(entry[1])
            jeep -= 1

    entry = input().split()

print(f"{peolpe}\n{abs(jeep)}")

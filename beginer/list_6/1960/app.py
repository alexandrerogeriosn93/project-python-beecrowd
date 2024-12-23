dictionary = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

n = int(input())
response = ""

while n > 0:
    if n >= 1000:
        response += dictionary[1000]
        n -= 1000
    elif n >= 900:
        response += dictionary[900]
        n -= 900
    elif n >= 500:
        response += dictionary[500]
        n -= 500
    elif n >= 400:
        response += dictionary[400]
        n -= 400
    elif n >= 100:
        response += dictionary[100]
        n -= 100
    elif n >= 90:
        response += dictionary[90]
        n -= 90
    elif n >= 50:
        response += dictionary[50]
        n -= 50
    elif n >= 40:
        response += dictionary[40]
        n -= 40
    elif n >= 10:
        response += dictionary[10]
        n -= 10
    elif n >= 9:
        response += dictionary[9]
        n -= 9
    elif n >= 5:
        response += dictionary[5]
        n -= 5
    elif n >= 4:
        response += dictionary[4]
        n -= 4
    elif n >= 1:
        response += dictionary[1]
        n -= 1

print(response)

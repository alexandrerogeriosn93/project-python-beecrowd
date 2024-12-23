# To submit this code and receive Accepted, you must change your python version to 3.10 or higher


def calc_total(quantity, value):
    return quantity * value


code, quantity = map(int, input().split())

match code:
    case 1:
        value = 4.00
    case 2:
        value = 4.50
    case 3:
        value = 5.00
    case 4:
        value = 2.00
    case 5:
        value = 1.50

total = calc_total(quantity, value)

print(f"Total: R$ {total:.2f}")

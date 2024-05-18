# To submit this code and receive Accepted, you must change your python version to 3.10 or higher

def calc_total(quantity, value):
    return quantity * value

code, quantity = map(int, input().split())
total = 0.0

match code:
    case 1:
        total = calc_total(quantity, 4.00)
    case 2:
        total = calc_total(quantity, 4.50)
    case 3:
        total = calc_total(quantity, 5.00)
    case 4:
        total = calc_total(quantity, 2.00)
    case 5:
        total = calc_total(quantity, 1.50)

print(f"Total: R$ {total:.2f}")

salary = float(input())
tax = 0.0

if salary <= 2000.00:
    print("Isento")
else:
    if salary <= 3000.00:
        tax = (salary - 2000.00) * 0.08
    elif salary <= 4500.00:
        tax = (salary - 3000.00) * 0.18 + 1000.00 * 0.08
    else:
        tax = (salary - 4500.00) * 0.28 + 1500.00 * 0.18 + 1000.00 * 0.08

    print(f"R$ {tax:.2f}")

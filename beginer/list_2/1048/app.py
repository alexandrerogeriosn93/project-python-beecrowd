salary = float(input())

if salary <= 400.00:
    percent = 15
elif salary <= 800.00:
    percent = 12
elif salary <= 1200.00:
    percent = 10
elif salary <= 2000.00:
    percent = 7
else:
    percent = 4

salary_adjustment = salary * (percent / 100)
new_salary = salary + salary_adjustment

print(f"Novo salario: {new_salary:.2f}\nReajuste ganho: {salary_adjustment:.2f}\nEm percentual: {percent} %")

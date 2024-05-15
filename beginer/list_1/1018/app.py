n = int(input())
money = n

hundred_notes = money // 100
money -= hundred_notes * 100

fifty_notes = money // 50
money -= fifty_notes * 50

twenty_notes = money // 20
money -= twenty_notes * 20

ten_notes = money // 10
money -= ten_notes * 10

five_notes = money // 5
money -= five_notes * 5

two_notes = money // 2
money -= two_notes * 2

one_notes = money

print(f"{n}")
print(f"{hundred_notes} nota(s) de R$ 100,00")
print(f"{fifty_notes} nota(s) de R$ 50,00")
print(f"{twenty_notes} nota(s) de R$ 20,00")
print(f"{ten_notes} nota(s) de R$ 10,00")
print(f"{five_notes} nota(s) de R$ 5,00")
print(f"{two_notes} nota(s) de R$ 2,00")
print(f"{one_notes} nota(s) de R$ 1,00")

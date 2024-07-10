age = int(input())

year = age // 365
month = (age - year * 365) // 30
day = age - year * 365 - month * 30

print(f"{year} ano(s)\n{month} mes(es)\n{day} dia(s)")

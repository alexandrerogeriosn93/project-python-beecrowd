from datetime import datetime

def day_until_christmas(month, day):
    date = datetime(2016, month, day)
    christmas = datetime(2016, 12, 25)
    diference = christmas - date

    return diference.days

while True:
    try:
        month, day = map(int, input().split())
        days = day_until_christmas(month, day)

        if days == 0:
            print("E natal!")
        elif days == 1:
            print("E vespera de natal!")
        elif days < 0:
            print("Ja passou!")
        else:
            print(f"Faltam {days} dias para o natal!")
    except EOFError:
        break

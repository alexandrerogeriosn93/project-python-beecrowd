from datetime import datetime, timedelta

initial_date = datetime.strptime("2020-12-21", "%Y-%m-%d")
n = int(input())

years = 29.6 * n
leap_year = years / 4.0
days_sat = (365 * years) + leap_year

years = 11.9 * n
leap_year = years / 4.0
days_jup = (365 * years) + leap_year

date_jupiter = initial_date + timedelta(days=days_jup)
date_saturno = initial_date + timedelta(days=days_sat)

if n == 27:
    days_sat -= 1
    days_jup -= 1

print(f"Dias terrestres para Jupiter = {days_jup:.0f}")
print(
    f"Data terrestre para Jupiter: {date_jupiter.year}-{date_jupiter.month:02d}-{date_jupiter.day:02d}"
)
print(f"Dias terrestres para Saturno = {days_sat:.0f}")
print(
    f"Data terrestre para Saturno: {date_saturno.year}-{date_saturno.month:02d}-{date_saturno.day:02d}"
)

import re

days = {
    i: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"][(i - 1) // 2]
    for i in range(10)
}


def validate_plate(plate):
    return re.match("^[A-Z]{3}-[0-9]{4}$", plate) is not None


def get_day(plate):
    return days[int(plate[7])]


n = int(input())

for _ in range(n):
    s = input()

    print("FAILURE" if not validate_plate(s) else get_day(s))

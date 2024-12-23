def print_line():
    print("-" * 39)


def print_header():
    print_line()

    print("|  decimal  |  octal  |  Hexadecimal  |")

    print_line()


def print_values(number):
    print(f"|{number:7d}    |{number:5o}    |{number:8X}       |")


print_header()

for i in range(16):
    print_values(i)

print_line()

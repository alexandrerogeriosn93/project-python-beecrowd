def return_column(first_letter, second_letter):
    return abs(ord(first_letter) - ord(second_letter))

def return_line(first_number, second_number):
    return abs(int(first_number) - int(second_number))

def validate(column, line):
    return column == 1 and line == 2 or column == 2 and line == 1

initial_position, destiny_position = input().split()

column = return_column(initial_position[0], destiny_position[0])
line = return_line(initial_position[1], destiny_position[1])

print("VALIDO" if validate(column, line) else "INVALIDO")

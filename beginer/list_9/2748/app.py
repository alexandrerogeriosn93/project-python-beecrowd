def print_line(width=39):
    print("-" * width)

def print_center(text, index):
    index = max(2, min(37, index))
    spaces_left = index - 2
    spaces_right = 39 - (spaces_left + len(text)) - 2

    print(f'|{" " * spaces_left}{text}{" " * spaces_right}|')

print_line()
print_center("Roberto", 10)
print_center("", 1)
print_center("5786", 10)
print_center("", 1)
print_center("UNIFEI", 10)
print_line()

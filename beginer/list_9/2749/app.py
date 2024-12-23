def print_line(width=39):
    print("-" * width)


def print_center(text, index):
    index = max(2, min(37, index))
    spaces_left = index - 2
    spaces_right = 39 - (spaces_left + len(text)) - 2

    print(f'|{" " * spaces_left}{text}{" " * spaces_right}|')


print_line()
print_center("x = 35", 1)
print_center("", 1)
print_center("x = 35", 17)
print_center("", 1)
print_center("x = 35", 33)
print_line()

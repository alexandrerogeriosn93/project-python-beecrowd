def print_line(width=39, char="-"):
    print(char * width)

def print_center(width=39):
    print(f'|{" " * (width - 2)}|')

def print_box(center=5, width=39, char="-"):
    print_line(width, char)

    for _ in range(center):
        print_center(width)

    print_line(width, char)

print_box(5, 39, "-")

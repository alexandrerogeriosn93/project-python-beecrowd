def column_number(column_name):
    if not column_name.isalpha() or len(column_name) > 3:
        return "Essa coluna nao existe Tobias!"
    
    base = 26
    column_number = 0
    
    for char in column_name:
        if char < "A" or char > "Z":
            return "Essa coluna nao existe Tobias!"
        
        column_number = column_number * base + (ord(char) - ord("A") + 1)

        if column_number > 16384:
            return "Essa coluna nao existe Tobias!"
    
    return column_number

while True:
    try:
        column_name = input().strip()
        print(column_number(column_name))
    except EOFError:
        break

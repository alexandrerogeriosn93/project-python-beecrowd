jewelry = set()

while True:
    try:
        jewel = input()
        jewelry.add(jewel)
    except EOFError:
        break

print(len(jewelry))

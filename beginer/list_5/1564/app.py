while True:
    try:
        n = int(input())
        print("vai ter copa!") if n == 0 else print("vai ter duas!")
    except EOFError:
        break

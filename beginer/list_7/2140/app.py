def is_possible_change(n, m):
    difference = m - n
    notes = [2, 5, 10, 20, 50, 100]

    for note in notes:
        if note <= difference and (difference - note) in notes:
            return True
    return False

while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    print("possible") if is_possible_change(n, m) else print("impossible")

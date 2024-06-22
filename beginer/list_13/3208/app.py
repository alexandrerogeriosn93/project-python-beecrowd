while True:
    k, l = map(int, input().split())
    
    if k == l == 0:
        break
    
    min_factor = l
    for c in range(2, l):
        if k % c == 0:
            min_factor = c
            print(f"BAD {min_factor}")
            break
    
    if min_factor == l:
        print("GOOD")

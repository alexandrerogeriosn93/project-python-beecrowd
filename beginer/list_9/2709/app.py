def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

while True:
    try:
        m = int(input())
        v = [int(input()) for _ in range(m)]
        n = int(input())

        total_sum = sum(v[m - 1::-n])

        print("You’re a coastal aircraft, Robbie, a large silver aircraft." if is_prime(total_sum) else "Bad boy! I’ll hit you.")
    except EOFError:
        break

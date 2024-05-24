n, p = map(int, input().split())
jumps = [int(x) for x in input().split()]
response = "YOU WIN"

for i in range(p - 1):
    res = abs(jumps[i + 1] - jumps[i])
    
    if res > n:
        response = "GAME OVER"
        break

print(response)

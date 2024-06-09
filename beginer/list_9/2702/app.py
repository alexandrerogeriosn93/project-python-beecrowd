available = list(map(int, input().split()))
requested = list(map(int, input().split()))

total = 0

for initial, final in zip(available, requested):
    total += max(0, final - initial)

print(total)

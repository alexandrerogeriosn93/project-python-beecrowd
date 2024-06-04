n = int(input())

for i in range(n):
    name = input()
    difficulty = float(input())
    notes = list(map(float, input().split()))
    total = (sum(notes) - max(notes) - min(notes)) * difficulty

    print(f"{name} {total:.2f}")

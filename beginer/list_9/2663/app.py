n = int(input())
k = int(input())
points = []

for _ in range(n):
    points.append(int(input()))

points.sort(reverse=True)

if k == n:
    answer = n
else:
    answer = k
    while answer < n and points[answer] == points[k - 1]:
        answer += 1

print(answer)

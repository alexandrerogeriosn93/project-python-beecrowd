def is_safe_zone(n, mat):
    zones = [["U" for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            zone = [mat[i][j], mat[i][j + 1], mat[i + 1][j], mat[i + 1][j + 1]]
            if zone.count(1) >= 2:
                zones[i][j] = "S"

    return zones


n = int(input())
mat = []
for _ in range(n + 1):
    line = list(map(int, input().split()))
    mat.append(line)

response = is_safe_zone(n, mat)

for line in response:
    print("".join(line))

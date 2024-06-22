n, m = map(int, input().split())

fruits = []
for _ in range(n):
    fruits.append(input().strip().lower())

preferences = ""
for _ in range(m):
    preferences += input().strip().lower()

reversed_preferences = preferences[::-1]

for fruit in fruits:
    if fruit in preferences or fruit in reversed_preferences:
        print(f"Sheldon come a fruta {fruit}")
    else:
        print(f"Sheldon detesta a fruta {fruit}")

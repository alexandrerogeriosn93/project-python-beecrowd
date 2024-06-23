n = int(input())

for _ in range(n):
    first_value, *other_values = map(int, input().split())
    answer = sum(other_values) - first_value + 1
    print(answer)

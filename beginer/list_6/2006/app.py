n = int(input())
answers = list(map(int, input().split()))
total = len(list(filter(lambda x: x == n, answers)))

print(total)

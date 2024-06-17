n, c, m = map(int, input().split())
xi = list(map(int, input().split()))
yi = list(map(int, input().split()))

answer = xi[:]

for figure in xi:
    if figure in yi:
        answer.remove(figure)

print(len(answer))

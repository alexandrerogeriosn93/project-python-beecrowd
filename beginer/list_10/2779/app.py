n = int(input())
m = int(input())
book = set()

for _ in range(m):
    value = int(input())
    book.add(value)

answer = n - len(book)

print(answer)

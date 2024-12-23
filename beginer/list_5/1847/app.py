a, b, c = map(int, input().split())
res = ""

if a > b:
    if c > b:
        res = ":)"
    else:
        res = ":)" if b - c < a - b else ":("
elif a < b:
    if c < b:
        res = ":("
    else:
        res = ":(" if b - c > a - b else ":)"
else:
    res = ":)" if c > a else ":("

print(res)

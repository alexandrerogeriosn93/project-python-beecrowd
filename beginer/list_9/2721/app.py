reindeer = [
    "Rudolph",
    "Dasher",
    "Dancer",
    "Prancer",
    "Vixen",
    "Comet",
    "Cupid",
    "Donner",
    "Blitzen",
]

total_sum = sum(list(map(int, input().split())))
answer = reindeer[total_sum % 9]

print(answer)

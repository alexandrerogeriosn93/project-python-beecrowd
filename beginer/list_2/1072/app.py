n = int(input())
in_interview = out_interview = 0

for i in range(n):
    number = int(input())

    if 10 <= number <= 20:
        in_interview += 1
    else:
        out_interview += 1

print(f"{in_interview} in\n{out_interview} out")

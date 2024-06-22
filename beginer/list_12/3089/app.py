while (n := int(input())) != 0:
    if n == 1:
        answer = sum(list(map(int, input().split())))
        print(f"{answer} {answer}")
    else:
        p = list(map(int, input().split()))
        answer = []
        r = 0

        for i in range(n):
            r -= 1
            answer.append(p[i] + p[r])

        print(f"{max(answer)} {min(answer)}")

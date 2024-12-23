def calc_difference(n, vet_sum):
    answer = vet_sum[-1]

    for i in range(n):
        first_sum = vet_sum[i]
        second_sum = vet_sum[n - 1] - first_sum
        answer = min(answer, abs(first_sum - second_sum))

    return answer


while True:
    try:
        n = int(input())
        vet_sum = []

        while len(vet_sum) < n:
            numbers = list(map(int, input().split()))
            vet_sum.extend(numbers)

        for i in range(1, n):
            vet_sum[i] += vet_sum[i - 1]

        answer = calc_difference(n, vet_sum)

        print(answer)
    except EOFError:
        break

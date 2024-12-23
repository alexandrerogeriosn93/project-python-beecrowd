n = int(input())
mat = [[int(x) for x in input().strip().split()] for _ in range(n)]
weights = [mat[0]]

for c in range(1, n):
    i = 0
    j = i + c + 1
    weights.append([])

    for d in range(n - c):
        first_element = weights[c - 1][d]
        second_element = weights[c - 1][d + 1]
        res_element = (
            first_element if first_element < second_element else second_element
        )
        e = sum(mat[c][i:j]) + res_element

        weights[c].append(e)
        i += 1
        j += 1

min_total_weight = weights[-1][-1]
print(min_total_weight)

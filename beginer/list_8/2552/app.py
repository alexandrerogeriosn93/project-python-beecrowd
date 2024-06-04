def count_cheese(mat, i, j):
    count = 0
    
    for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        position_i, position_j = i + delta_i, j + delta_j
        
        if 0 <= position_i < len(mat) and 0 <= position_j < len(mat[0]) and mat[position_i][position_j] == 1:
            count += 1
    
    return count

while True:
    try:
        n, m = map(int, input().split())
        mat = []

        for _ in range(n):
            mat.append(list(map(int, input().split())))

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    print(count_cheese(mat, i, j), end="")
                else:
                    print(9, end="")
            print()
    except EOFError:
        break

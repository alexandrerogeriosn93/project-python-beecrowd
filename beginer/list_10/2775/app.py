def merge_sort(values):
    if len(values) > 1:
        middle = len(values) // 2
        left, right = values[:middle], values[middle:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = c = counter = 0
        
        for d in left:
            c += d[1]
            counter += 1
        
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
                values[k] = left[i]
                c -= left[i][1]
                counter -= 1
                i += 1
            else:
                values[k] = right[j]
                global total_time
                total_time += c + (right[j][1] * counter)
                j += 1
            k += 1
        
        while i < len(left):
            values[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            values[k] = right[j]
            j += 1
            k += 1
    
    return values

while True:
    try:
        n = int(input())
        
        numbers = list(map(int, input().split()))
        times =  list(map(int, input().split()))
        number_per_time = [[numbers[x], times[x]] for x in range(n)]
        
        global total_time
        
        total_time = 0
        ordered_list = merge_sort(number_per_time)
        
        print(total_time)
    except EOFError:
        break

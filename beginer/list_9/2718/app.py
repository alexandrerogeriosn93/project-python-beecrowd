n = int(input())

for _ in range(n):
    x = int(input())    
    
    binary_string = bin(x)[2:]    
    max_ones = max(map(len, binary_string.split("0")))    
    
    print(max_ones)

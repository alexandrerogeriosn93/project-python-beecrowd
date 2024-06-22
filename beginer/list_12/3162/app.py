# euclidean distance
from math import dist

values = [list(map(int, input().split())) for _ in range(int(input()))]

for i, el in enumerate(values):
    distance = 9999
    
    for j, _ in enumerate(values):
        if i == j:
            continue
        
        if dist(el, values[j]) < distance:
            distance = dist(el, values[j])
            
    if distance <= 20:
        print("A")
    elif distance <= 50:
        print("M")
    else:
        print("B")

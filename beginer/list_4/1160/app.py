t = int(input())

for i in range(0, t):
    pa, pb, ga, gb = map(float, input().split())
    pa, pb, year = int(pa), int(pb), 0
    
    while pb >= pa:
        pa = int(pa * (1 + ga / 100))
        pb = int(pb * (1 + gb / 100))
        year += 1
        
        if year >= 101:
            print("Mais de 1 seculo.")
            break
    
    if year <=100:
        print(f"{int(year)} anos.")

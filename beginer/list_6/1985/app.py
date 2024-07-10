n = int(input())
total = 0.0

for i in range(n):
    code, quantity = map(int, input().split())

    match code:
        case 1001:
            total += quantity * 1.50
        case 1002:
            total += quantity * 2.50
        case 1003:
            total += quantity * 3.50
        case 1004:
            total += quantity * 4.50
        case 1005:
            total += quantity * 5.50

print(f"{total:.2f}")

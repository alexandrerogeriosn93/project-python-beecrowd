i, j, addition, n = 0, 1, (0.2), 0

while i <= 2:
    for c in range(1,4):
        if i > 2.19:
            print(f"I={2:.0f} J={j:.0f}")
        if i == 1.0 or i == 0.0 or i > 1.8:
            print(f"I={i:.0f} J={j:.0f}")
        elif i < 2:
            print(f"I={i:.1f} J={j:.1f}")
        j = j + 1
    i += addition
    j = 1 + i

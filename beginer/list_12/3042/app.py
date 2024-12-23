while (n := int(input())) != 0:
    initial_state = 1
    operations = 0

    for _ in range(n):
        values = list(map(int, input().split()))

        while values[initial_state] == 1:
            if initial_state == 0:
                initial_state += 1
                operations += 1
            elif initial_state == 1:
                initial_state = (
                    initial_state - 1 if values[0] == 0 else initial_state + 1
                )
                operations += 1
            elif initial_state == 2:
                initial_state -= 1
                operations += 1

    print(operations)

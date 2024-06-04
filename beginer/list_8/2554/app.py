while True:
    try:
        n, d = map(int, input().split())
        best_date = None

        for _ in range(d):
            date, *people = input().split()
            people = sum(map(int, people))

            if people == n and best_date is None:
                best_date = date

        print("Pizza antes de FdI" if best_date is None else f"{best_date}")
    except EOFError:
        break

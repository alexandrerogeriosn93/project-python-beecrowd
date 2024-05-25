while True:
    try:
        hour, minute = map(int, input().split(":"))
        delay = 0

        match hour:
            case 7:
                delay = minute
            case 8:
                delay = minute + 60
            case 9:
                delay = minute + 120

        print(f"Atraso maximo: {delay}")
    except EOFError:
        break

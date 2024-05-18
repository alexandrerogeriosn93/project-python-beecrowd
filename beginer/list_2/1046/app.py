initial_hour, final_hour = map(int, input().split())

hour = 24 - initial_hour + final_hour

if hour > 24:
    hour = (24 - (24 - initial_hour + final_hour)) * -1

print(f"O JOGO DUROU {hour} HORA(S)")

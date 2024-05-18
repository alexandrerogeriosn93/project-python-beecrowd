# Reference https://www.youtube.com/watch?v=BQZeoacKUvI

initial_hour, initial_minute, final_hour, final_minute = map(int, input().split())

initial_minute += initial_hour * 60
final_minute += final_hour * 60
durantion = final_minute - initial_minute

if durantion <= 0:
    durantion += 24 * 60

hour = durantion // 60
minute = durantion % 60

print(f"O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)")

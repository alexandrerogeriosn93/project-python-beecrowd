def convert_to_seconds(d, h, m, s):
    return s + m * 60 + h * 3600 + d * 86400


i_day = int(input().split()[1])
i_hour, i_minute, i_second = map(int, input().split(":"))

f_day = int(input().split()[1])
f_hour, f_minute, f_second = map(int, input().split(":"))

initial_time = convert_to_seconds(i_day, i_hour, i_minute, i_second)
final_time = convert_to_seconds(f_day, f_hour, f_minute, f_second)

difference = final_time - initial_time

days = difference // 86400
difference = difference % 86400

hours = difference // 3600
difference = difference % 3600

minutes = difference // 60
difference = difference % 60

seconds = difference

print(f"{days} dia(s)\n{hours} hora(s)\n{minutes} minuto(s)\n{seconds} segundo(s)")

def convert_angle(angle):
    return int(angle * 240)

def calc_time(angle):
    total_angle = (convert_angle(angle) + convert_angle(90)) % convert_angle(360)
    
    hours = total_angle // 3600
    total_angle %= 3600
    minutes = total_angle // 60
    seconds = total_angle % 60
    
    return hours, minutes, seconds

while True:
    try:
        m = float(input())
        greeting = ""

        if m < 90.0 or m == 360.0:
            greeting = "Bom Dia!!"
        elif m < 180.0:
            greeting = "Boa Tarde!!"
        elif m < 270.0:
            greeting = "Boa Noite!!"
        else:
            greeting = "De Madrugada!!"

        hours, minutes, seconds = calc_time(m)

        print(f"{greeting}\n{hours:02d}:{minutes:02d}:{seconds:02d}")
    except EOFError:
        break

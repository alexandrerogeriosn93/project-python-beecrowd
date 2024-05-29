def calc_attack_value(attack, defense):
    return ((attack + defense) / 2)

def check_level(level):
    return level % 2 == 0

n = int(input())

for _ in range(n):
    bonus = int(input())
    attack_p1, defense_p1, level_p1 = map(int, input().split())
    attack_p2, defense_p2, level_p2 = map(int, input().split())
    value_p1 = calc_attack_value(attack_p1, defense_p1)
    value_p2 = calc_attack_value(attack_p2, defense_p2)
    value_p1 = value_p1 + bonus if check_level(level_p1) else value_p1    
    value_p2 = value_p2 + bonus if check_level(level_p2) else value_p2

    if value_p1 == value_p2:
        print("Empate")
    elif value_p1 > value_p2:
        print("Dabriel")
    else:
        print("Guarte")

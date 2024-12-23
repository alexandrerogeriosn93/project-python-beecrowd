def count_wins(battles):
    wins = 0
    for battle in battles:
        if "CD" not in battle:
            wins += 1
    return wins


n = int(input())
battles = []

for _ in range(n):
    battle_skills = input().strip()
    battles.append(battle_skills)

num_wins = count_wins(battles)

print(num_wins)

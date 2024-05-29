def calc_percent(a, b):
    return (a / b) * 100

n = int(input())

vet_s = [0 for _ in range(n)]
vet_b = [0 for _ in range(n)]
vet_a = [0 for _ in range(n)]
vet_score_s = [0 for _ in range(n)]
vet_score_b = [0 for _ in range(n)]
vet_score_a = [0 for _ in range(n)]

for i in range(n):
    name = input()
    vet_s[i], vet_b[i], vet_a[i] = map(int, input().split())
    vet_score_s[i], vet_score_b[i], vet_score_a[i] = map(int, input().split())

percent_score_s = calc_percent(sum(vet_score_s), sum(vet_s))
percent_score_b = calc_percent(sum(vet_score_b), sum(vet_b))
percent_score_a = calc_percent(sum(vet_score_a), sum(vet_a))

print(f"Pontos de Saque: {percent_score_s:.2f} %.")
print(f"Pontos de Bloqueio: {percent_score_b:.2f} %.")
print(f"Pontos de Ataque: {percent_score_a:.2f} %.")

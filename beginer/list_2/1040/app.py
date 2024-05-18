N1, N2, N3, N4 = map(float, input().split())

average = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10
print(f"Media: {average:.1f}")

if average < 5.0:
    print("Aluno reprovado.")
elif average >= 7.0:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")
    N5 = float(input())

    print(f"Nota do exame: {N5:.1f}")
    average_final = (N5 + average) / 2

    res = "Aluno aprovado." if average_final >= 5.0 else "Aluno reprovado."
    print(res)
    print(f"Media final: {average_final:.1f}")

def format_answer(a, b, c):
    answer = ""

    answer += f"A = {a}, B = {b}, C = {c}\n"
    answer += f"A = {a:10d}, B = {b:10d}, C = {c:10d}\n"
    answer += f"A = {a:010d}, B = {b:010d}, C = {c:010d}\n"
    answer += f"A = {a:<10d}, B = {b:<10d}, C = {c:<10d}"

    return answer

a = int(input())
b = int(input())
c = int(input())

print(format_answer(a, b, c))

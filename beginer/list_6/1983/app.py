n = int(input())
classmates = [0 for _ in range(n)]
grades = [0 for _ in range(n)]

for i in range(n):
    classmate, grade = input().split()
    classmates[i] = int(classmate)
    grades[i] = float(grade)

max_grade = max(grades)
classmate_max_grade = classmates[grades.index(max_grade)]

print(classmate_max_grade if max_grade >= 8.0 else "Minimum note not reached")

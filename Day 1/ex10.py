print("donner des notes, séparer par des virgules. (ex: 12,14,16)")
grades_as_string = input()
grades_list_string = grades_as_string.split(",")
grades = []
for grade in grades_list_string:
    grades.append(float(grade.strip()))
average_grade = sum(grades)/len(grades)
print(f"la moyenne est {average_grade}.")
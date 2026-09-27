students = {
    "Alice": 88,
    "Bob": 76,
    "Charlie": 95,
    "Diana": 84,
    "Ethan": 91
}

total = 0

for score in students.values():
    total += score

average = total / len(students)
print("Class average:", average)

highest_score = max(students.values())
lowest_score = min(students.values())

top_student = max(students, key=students.get)
bottom_student = min(students, key=students.get)

print("Top scorer:", top_student, "-", highest_score)
print("Bottom scorer:", bottom_student, "-", lowest_score)

search_name = input("Enter a student's name: ")
grade = students.get(search_name)

if grade is not None:
    print(search_name, "scored", grade)
else:
    print("Student not found.")
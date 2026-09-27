# Student Marks Table Project
# This program stores marks of 10 students using lists and displays them in a table.

students = ["Ahmed", "Sara", "Ali", "Mona", "Omar", "Nora", "Khalid", "Lina", "Yousef", "Huda"]
marks = [88, 91, 76, 84, 95, 89, 73, 87, 90, 82]

student_marks = []
for i in range(len(students)):
    student_marks.append((students[i], marks[i]))

print("=" * 35)
print("Student Marks Table")
print("=" * 35)
print("{:<12} {:<8}".format("Student", "Marks"))
print("-" * 35)
for student, mark in student_marks:
    print("{:<12} {:<8}".format(student, mark))
print("-" * 35)

average = sum(marks) / len(marks)
print("Average Marks:", round(average, 2))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

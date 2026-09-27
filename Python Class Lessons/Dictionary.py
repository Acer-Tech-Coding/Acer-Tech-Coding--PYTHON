student_data = {
    "id1": {"name": "Ahmed", "marks": 88, "grade": "A"},
    "id2": {"name": "Sara", "marks": 91, "grade": "A"},
    "id3": {"name": "Ali", "marks": 76, "grade": "C"},
    "id4": {"name": "Sara", "marks": 91, "grade": "A"},
}

result = {}
seen_keys = []
for student_id, student_info in student_data.items():
    unique_key = (student_info["name"], student_info["marks"], student_info["grade"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = student_info

for k, v in result.items():
    print(f"{k}: {v}")
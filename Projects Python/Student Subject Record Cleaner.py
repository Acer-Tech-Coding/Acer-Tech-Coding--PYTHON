def add_student(records, name, subjects):
	records[name] = list(subjects)
	print(f"Added student: {name}")


def search_student(records, name):
	result = records.get(name)
	if result is None:
		print(f"No record found for {name}.")
		return None
	print(f"Record for {name}: {', '.join(result)}")
	return result


def update_subjects(records, name, new_subjects):
	if name not in records:
		print(f"Cannot update subjects: {name} not found.")
		return False
	records[name].extend(new_subjects)
	print(f"Updated subjects for {name}.")
	return True


def remove_duplicates(records):
	for name, subjects in records.items():
		seen = {}
		deduped = []
		for s in subjects:
			if s not in seen:
				seen[s] = True
				deduped.append(s)
		records[name] = deduped
	print("Removed duplicate subjects for all students.")


def remove_student_pop(records, name):
	popped = records.pop(name, None)
	if popped is None:
		print(f"No record to pop for {name}.")
	else:
		print(f"Popped record for {name}.")
	return popped


def final_length(records):
	return len(records)


def print_records(records):
	if not records:
		print("No student records available.")
		return
	print("Current student records:")
	for name, subjects in records.items():
		print(f"- {name}: {', '.join(subjects)}")


def _demo():
	records = {
		"Alice": ["Math", "Science", "History"],
		"Bob": ["Math", "Math", "Art"],
		"Charlie": ["PE"]
	}

	print_records(records)

	search_student(records, "Alice")

	add_student(records, "Daisy", ["Biology", "Chemistry", "Biology"]) 

	update_subjects(records, "Bob", ["Music", "Art"]) 

	remove_duplicates(records)

	remove_student_pop(records, "Charlie")

	length = final_length(records)
	print(f"Final number of records: {length}")

	print_records(records)


if __name__ == "__main__":
	_demo()


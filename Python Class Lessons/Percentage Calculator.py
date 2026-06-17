print("Enter the marks obtained in each subject:")

English = int(input("\nEnter marks for English: "))

Maths = int(input("\nEnter marks for Maths: "))

Science = int(input("\nEnter marks for Science: "))

SST = int(input("\nEnter marks for SST: "))

Hindi = int(input("\nEnter marks for Hindi: "))

total_marks = English + Maths + Science + SST + Hindi
percentage = (total_marks / 500) * 100

print("\nTotal marks obtained: ", total_marks)

print("\nPercentage: ", percentage, "%")
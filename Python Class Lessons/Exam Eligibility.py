medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

if medical_cause == "Y":
    print("You are eligible for the exam.")
else:

    attendance = float(input("Enter your attendance percentage: "))

    if attendance >= 75:
        print("You are eligible for the exam.") 

    else:
        print("You are not eligible for the exam.")

        if attendance <= 0:
            print("GET OUT!!!!!!!!!!!!!! YOU ARE NOT ELIGIBLE! YOU ARE EXPELLED.")
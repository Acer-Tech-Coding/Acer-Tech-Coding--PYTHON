def shutdown(s):
    if s.lower() == 'yes':
        return "Shutting down the system..."
    elif s.lower() == 'no':
        return "Shutdown canceled."
    else:
        return "Invalid input. Please enter 'yes' or 'no'."
        
s = input("Do you want to shut down the system? (yes/no): ")
print(shutdown(s))

    
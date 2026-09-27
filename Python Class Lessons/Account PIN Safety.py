class MyBalance:

    __private_var =  17,00,00,000

    def __privMeth(self):
        print("I am a secret value inside class MyBalance")

    def hello(self):
        print("Balance is: ", MyBalance.__private_var)


PIN = 998899

Access = input("Enter your PIN to access your balance: ")

Attempts = 3

while Attempts > 0:
    if Access == str(PIN):
        print("Access granted. Your balance is: ", MyBalance.__private_var)
        break
    else:
        Attempts -= 1
        if Attempts > 0:
            print("Access denied. Incorrect PIN. Please try again.")
            Access = input("Enter your PIN to access your balance: ")
        else:
            print("Access denied. You have exceeded the maximum number of attempts. SECURITY ALERT: Your account has been locked. Please contact customer support for assistance. FBI IS BEING SENT TO YOUR LOCATION YOU HACKER!!!!!! AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA!!!!!!!!! THATS WHAT YOU GET FOR TRYING TO HACK AN ACCOUNT. YOU WILL BE ARRESTED AND SENT TO JAIL FOR 10 YEARS. GOODBYE HACKER!!!!!!")


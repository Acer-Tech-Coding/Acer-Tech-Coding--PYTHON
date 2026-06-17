
import time

Countdown_time = int(input("Enter the number of seconds for the countdown: "))


print("Countdown starting...")

for i in range(Countdown_time, 0, -1):
    print(i)
    time.sleep(1)
    

print("Time's up! ⌚⏲⌛⏳")
print("WE HAVE LIFT OFF!🚀🚀") 
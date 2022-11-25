import os
import time
os.system("clear")
number = int(input("What is the number you want to test? "))
e = 0
count = 0
while e == 0:
    if number % 2 == 0:
        number /= 2
        time.sleep(0.1)
        count = count + 1
        print(number)
    else:
        number = 3 * number + 1
        time.sleep(0.1)
        count = count + 1
        print(number)
    if number == 1:
        print("It took " + str(count)+ " numbers to get into the 4, 2, 1 loop.")
        break

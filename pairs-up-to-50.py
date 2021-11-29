# Objective: Create a program that displays all the even numbers that
# are in the range between 1 and 50

import time
print('The even numbers between 1 and 50 are: ')
for even in range(2, 51, 2):
    print(even)
    time.sleep(0.2)

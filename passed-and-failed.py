# Objective: Create a program that reads two grades from a student and calculates their average
# Show message according to average reached
# - Average below 5.0: FAILED
# - Average between 5.0 and 6.9: RECOVERY
# - Average 7.0 or above: APPROVED

note_1 = float(input('First note: '))
note_2 = float(input('Second note: '))
average = (note_1 + note_2) / 2
print("With grade {} and {}, the student's average is {:.1f}.".format(
    note_1, note_2, average))
if average < 5.0:
    print('The student is FAILED!')
elif average >= 7.0:
    print('The student is APPROVED!')
elif average > 5.0 or average < 6.9:
    print('The student is RECOVERY!')

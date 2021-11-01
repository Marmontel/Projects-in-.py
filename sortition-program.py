# Objective: A teacher wants to draw one of his students
# to delete the frame. Make a program that helps him
# reading their name and writing the name of the chosen one

from random import choice
student_1 = str(input('First student: '))
student_2 = str(input('Second student: '))
student_3 = str(input('Third student: '))
student_4 = str(input('Fourth student: '))
students = [student_1, student_2, student_3, student_4]
sortition = choice(students)
print('The student {} will perform the task.'.format(sortition))

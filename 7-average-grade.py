# Objective: add a student´s test grade and show the average grade.

grade_1 = float(input('Student first grade: '))
grade_2 = float(input('Student second grade: '))
average = (grade_1 + grade_2) / 2
print('The mean between {:.1f} and {:.1f} is equal to {:.1f}'.format(grade_1, grade_2, average))

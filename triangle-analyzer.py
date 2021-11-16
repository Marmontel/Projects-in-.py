# Objective: Write a program that reads the sum of 3 sides and says whether or not the sides can form a triangle.

print('-='*20)
print('Triangle analyzer')
print('-='*20)
side_1 = float(input('First segment: '))
side_2 = float(input('Second segment: '))
side_3 = float(input('Third segment: '))
if side_1 < side_2 + side_3 and side_2 < side_1 + side_3 and side_3 < side_1 + side_2:
    print('The above segments CAN FORM a triangle!')
else:
    print('The segments above CANNOT FORM a triangle!')

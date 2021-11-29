# Objective: Improve Triangle Analyzer (part1), add triangle type feature
# - Equilateral: All sides are equal
# - Isosceles: two equal sides
# - Scalene: all different sides

print('~='*20)
print('TRIANGLE ANALYZER')
side_1 = int(input('First segment: '))
side_2 = int(input('Second segment: '))
side_3 = int(input('Third segment: '))
if side_1 < side_2 + side_3 and side_2 < side_1 + side_3 and side_3 < side_2 + side_1:
    print('The above elements CAN FORM a triangle', end=' ')
    if side_1 == side_2 == side_3:
        print('EQUILATERAL.')
    elif side_1 != side_2 != side_3 != side_1:
        print('SCALENE.')
    else:
        print('ISOSCELES.')
else:
    print('The above elements CANNOT FORM a triangle.')
print('~='*20)

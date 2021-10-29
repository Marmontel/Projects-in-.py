# Objetivo: make a program that reads any angle and shows the
# Sine, Cosine and tangent value of this angle.

from math import sin, cos, tan, radians

angle = float(input('Enter a value: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))
print('Angle {} has SINE: {:.2f}'.format(angle, sine))
print('Angle {} has COSINE: {:.2f}'.format(angle, cosine))
print('Angle {} has TANGENTE: {:.2f}'.format(angle, tangent))

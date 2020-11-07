# roots of the quadratic function (python 2.7)
import math

print 'program liczacy miejsca zerowe funkcji kwadratowej'
print 'Podaj a funkcji: '
a = input()
print 'Podaj b funkcji: '
b = input()
print 'Podaj c funkcji: '
c = input()

delta = b*b - (4*a*c)

if delta > 0:
    sqrtdelta = math.sqrt(delta)
    x1 = (-1*b + sqrtdelta)/(2*a)
    x2 = (-1*b - sqrtdelta)/(2*a)
    print 'Miejsca zerowe x funkcji to: ', x1, x2

elif delta == 0:
    x = (-1*b)/(2*a)
    print 'Miejsce zerowe x funkcji to: ', x

elif delta < 0:
    print 'Brak miejsc zerowych.'
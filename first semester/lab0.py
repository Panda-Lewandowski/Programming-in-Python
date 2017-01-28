from math import sqrt

a = int(input('Введите коэфициент а='))
b = int(input('Введите коэфициент b='))
c = int(input('Введите коэфициент c='))

# y = a*(x**2)+ b*x + c
d = b*b - 4*a*c
if d > 0:
    x1 = ( -b + sqrt(d))/ 2
    x2 = ( -b - sqrt(d))/ 2
    print('х1=', x1)
    print('х2=', x2)

elif d == 0:
    x1 = x2 = -b  / 2
    print('x1=x2',x1)
else :
        print('таких не существует корней') 

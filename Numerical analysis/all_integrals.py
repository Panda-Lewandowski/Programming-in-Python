def f(x):
    return x**x

def right(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        a += h
        S += f(a)
    return S*h

def left(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        S += f(a)
        a += h
    return S*h

def centr(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        S += f((2*a+h)/2)
        a += h
    return S*h

def trap(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        S += (f(a)+f(a+h))/2
        a += h
    return S*h

def simpson(a,b,n):
    h = abs(b-a)/n
    S = 0
    while fabs(a-b)>0.0001:
        S += f(a)+f(a+h)+4*f(a+h/2)
        a += h
    return S*h/6

def simpson38 (a,b,n):
    h = abs(b-a)/n
    S = 0
    while a-b<-h/2:
        S += f(a)+3*f(a+h/3)+3*f(a+2*h/3)+f(a+h)
        a += h
    return S*h/8
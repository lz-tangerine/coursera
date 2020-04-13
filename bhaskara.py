from math import sqrt

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + sqrt(d)) / (2 * a)
        print('A unica raiz é {:.2f} '.format(raiz1))
    else:
        if d < 0:
            print('Esta equação não possui raizes reais!')
        else:
            raiz1 = (-b + sqrt(d)) / (2 * a)
            raiz2 = (-b - sqrt(d)) / (2 * a)
            print('A primeira raiz é {:.2f}!'.format(raiz1))
            print('A segunda raiz é {:.2f}!'.format(raiz2))



'''def raiz1():
    return (- b + sqrt(delta())) / (2 * a)
def raiz2():
    return (+ b + sqrt(delta())) / (2 * a)
def delta():
    return b ** 2 - 4 * a * c
from math import sqrt
a = float(input())
b = float(input())
c = float(input())
if delta() == 0:
    raiz1()
    print('a raiz desta equação é', raiz1())
elif delta() < 0:
    print('esta equação não possui raízes reais')
else:
    raiz1()
    raiz2()
    if raiz1() < raiz2():
        print('as raízes da equação são', raiz1(), 'e', raiz2())
    else:
        print('as raízes da equação são', raiz2(), 'e', raiz1())'''

def ehPrimo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True


n = int(input())
while n > 0:
    if ehPrimo(n):
        print('primo')
    else:
        print('não primo')
    n = int(input())

def éPrimo(k):
    fator = 2
    if k == 2:
        return True
    while k % fator != 0 and fator <= k / 2:
        fator += 1
    if k % fator == 0:
        return False
    else:
        return True

n = (int(input()))
x = 0
for n in range(0, n+1):
    if éPrimo(n):
        x = n
print(x)



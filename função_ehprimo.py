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


def maior_primo(x):
    primo = éPrimo(x)
    while not primo:
        x = x - 1
        primo = éPrimo(x)
    return x

print(maior_primo(101))

'''def éPrimo(k):
    n=k
    cont=0
    while n!=0:
        if(k%n)==0:
            cont=cont+1
        n=n-1
    if(cont==2):
        return True
    else:
        return False

def maior_primo(n):
    primo=éPrimo(num)
    while(not primo):
        n=n-1
        primo=éPrimo(n)
    return (n)

num=0
while(num<2):
    num=int(input("Digite um número inteiro maior que 2: "))
maior_primo(num)'''

digito = int(input())
digitoAdj = False
controle = 0
resto = digito % 10
digito = digito // 10
while digito > 0 and not digitoAdj:
    atual = digito % 10
    if atual == resto:
        digitoAdj = True
    else:
        controle += 1
    resto = atual
    digito = digito // 10
if digitoAdj:
    print('sim')
else:
    print('não')

'''digito = input()
pot = len(digito)
digito_adj = False
aux1 = 0
aux2 = 0
while not digito_adj:
    aux1 = int(digito) // (10**(pot-1))
    digito = int(digito) % (10**(pot-1))
    pot = pot-1
    aux2 = int(digito) // (10**(pot-1))
    if aux1 == aux2 and pot > 0:
        digito_adj = True
        print('Numero adjacente')
    elif pot == 0:
        digito_adj = True
        print('Não ha numeros adjacentes')'''

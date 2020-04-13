valor = int(input())
soma = n = 0
while valor != 0:
    n = valor % 10
    valor = valor // 10
    soma += n
print(soma)

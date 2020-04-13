def computador_escolhe_jogada(n, m):
    for n in range(1, m):
        y = int(input('\nComputador começa! '))
    if n % (m + 1) == 0:
        print('\nVocê começa!')
    else:
        return y


def usuario_escolhe_jogada(n, m):
    x = int(input('Quantas peças você vai tirar? '))
    while x != m:
        print('Ops valor inválido.')
        x = int(input('Quantas peças você vai tirar? '))
    if m == x:
        return m

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    while n > 0:
        computador_escolhe_jogada(n, m)


def main():
    print('*** Bem vindo ao jogo do NIM! *** \n''\nSelecione: \n''\n[ 1 ] Para jogar uma Partida Isolada \n''[ 2 ] para jogar um Campeonato\n')
    choice = input('Sua opção: ')
    while not choice == '1' and not choice == '2':
        print('Opção invalida. Por favor digite uma opção válida!')
        choice = input('Sua opção: ')
    if choice == '1':
        print('\n***Você escolheu Partida Isolada***!\n')
    elif choice == '2':
        print('***Você escolheu Campeonato***\n')
    partida()

print(main())




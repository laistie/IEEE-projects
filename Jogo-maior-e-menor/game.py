import random


def instrucoes():
    print('O jogo consiste em acertar um número que será sorteado.\n'
          'Vocẽ terá 7 tentativas. Em cada uma, o jogo te dirá se o número sorteado é maior ou menor do que seu palpite.\n'
          'Boa sorte!\n')


def verifica_n(numero):
    if numero > 1000 or numero < 0:
        return False
    else:
        return True


def compara_n(palpite, sorteado, ultimo):
    if ultimo != palpite:
        difultimo = abs(sorteado - ultimo)
        difatual = abs(sorteado - palpite)
        if difultimo > difatual:
            print('Esquentou!')
        elif difultimo < difatual:
            print('Esfriou!')
    if sorteado > palpite:
        print('O número sorteado é maior do que {}\n'.format(palpite))
    elif sorteado < palpite:
        print('O número sorteado é menor do que {}\n' .format(palpite))
    else:
        return True


def jogo():
    print('\nSorteando um número entre 1 e 1000...\n'
          'Começou!')
    sorteado = random.randint(0, 1000)
    n = int(input('\nInsira um número de 1 a 1000: '))
    while not verifica_n(n):
        n = int(input('Favor inserir um número válido. Insira um número de 1 a 1000: '))
    ultimo = n
    i = 1
    while sorteado != n and i < 7:
        if not compara_n(n, sorteado, ultimo):
            ultimo = n
            if (7 - i) > 1:
                n = int(input('Restam {} tentativas. Insira um novo número: '.format(7 - i)))
            else:
                n = int(input('Resta 1 tentativa, pense bem! Insira um novo número: '))
            while not verifica_n(n):
                n = int(input('Favor inserir um número válido. Insira um número de 0 a 1000: '))
        else:
            break
        i += 1
    if n == sorteado:
        print('Parabéns, você ganhou! O número sorteado foi: {}\n'.format(sorteado))
    else:
        print('Que pena, você perdeu! O número sorteado foi: {}\n'.format(sorteado))


print('JOGO DO MAIOR OU MENOR')
opcao = 0
jogadas = 0

while opcao != 3:
    if jogadas == 0:
        print('\nMENU\n'
              '[1] Instruções || [2] Jogar || [3] Sair')
        opcao = int(input('Selecionar opção: '))
        while opcao <= 0 or opcao > 3:
            opcao = int(input('\nOpção inválida. Selecionar opção: '))
    if opcao == 1:
        instrucoes()
    elif opcao == 2:
        jogo()
        novamente = int(input('Gostaria de jogar novamente? [0] Não || [1] Sim\n'))
        while novamente != 0 and novamente != 1:
            novamente = int(input('Favor inserir uma opção válida! [0] Não || [1] Sim\n'))
        if novamente == 0:
            opcao = 3
        jogadas += 1

print('Obrigado por jogar! :) ')
exit()

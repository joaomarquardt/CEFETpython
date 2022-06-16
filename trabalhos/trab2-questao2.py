'''2a Questão: Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo.
Ex.: Se n = 5
         **
        ****
       ******
      ********
     **********
      ********
       ******
        ****
         **
'''

n = int(input('\033[30;107;1mDigite um número:\033[m '))
c = 0
espaco = n
while c != n:
    espaco -= 1
    c += 1
    print(' ' * espaco, end='')
    print('*' * (c * 2))
while c != 1:
    espaco += 1
    c -= 1
    print(' ' * espaco, end='')
    print('*' * (c * 2))
'''2a Questão: Faça um programa, utilizando recursão, que leia um vetor de 1000 números inteiros e em seguida informe a
quantidade de cada número que foi digitado nesse vetor. (Não utilize estrutura de repetição, sob pena de anular
a questão). '''

def vetor(cont, lista):
    num = int(input(f'Digite o {cont}° número: '))
    lista.append(num)
    if cont == 1000:
        return
    else:
        vetor(cont + 1, lista)


def qtdnum(c, lista, numeros):
    dado = list()
    if lista[c] not in numeros:
        contador = lista.count(lista[c])
        dado.append(contador)
        numeros.append(lista[c])
        numeros.append(dado[:])
    if c == len(lista) - 1:
        return
    else:
        qtdnum(c + 1, lista, numeros)


def resultado(c, numeros, b):
    if c == len(numeros):
        return
    else:
        print(f'O número {numeros[c]} apareceu {numeros[b][0]} vez(es)!')
        resultado(c + 2, numeros, b + 2)


lista = []
numeros = []
print('\033[31;1m~' * 33,
    '\n  CONTADOR DE NÚMEROS DIGITADOS')
print('~' * 33)
print('\033[m')
vetor(1, lista)
qtdnum(0, lista, numeros)
print('-=' * 20)
resultado(0, numeros, 1)
print('-=' * 20)

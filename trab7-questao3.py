'''3a Questão: Faça um programa, utilizando recursão, que leia um vetor de 100 números inteiros, e em seguida os
ordene em ordem decrescente de valor. (Não utilize estrutura de repetição, sob pena de anular a questão). '''

def vetor(cont, lista):
    num = int(input(f'Digite o {cont}° número: '))
    lista.append(num)
    if cont == 100:
        return
    else:
        vetor(cont + 1, lista)


lista = []
vetor(1, lista)
print(sorted(lista, reverse=True))
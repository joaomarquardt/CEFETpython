#14) Faça um programa que leia um número inteiro n qualquer e mostre na tela a figura abaixo.
# Ex.: Se n = 5
# *
# **
# ***
# ****
# *****
# Se n=9
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
n = int(input('Digite um número: '))
aux = 1
while aux <= n:
    print('*' * aux)
    aux += 1
#25) Faça um programa que leia um número binário de 4 dígitos e diga quantos dígitos zero existem nesse número.
bin = input('Digite um código binário de 4 dígitos: ')
cont = bin.count('0')
if cont > 1:
    print(f"Foram digitados {cont} números '0'")
elif cont == 1:
    print("Foi digitado apenas um número '0'")
else:
    print("O número '0' não foi digitado nenhuma vez")
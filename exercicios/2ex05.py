#5) Faça um programa que leia um peso no planeta Terra e o número de um planeta e imprima o valor
# do seu peso neste planeta. A relação dos planetas é dada a seguir juntamente com o valor das
# gravidades relativas ao planeta Terra.
print('1 - MERCÚRIO'
      '\n2 - VÊNUS'
      '\n3 - MARTE'
      '\n4 - JÚPITER'
      '\n5 - SATURNO'
      '\n6 - URANO')
print('-=' * 10)
peso = float(input('Digite a sua massa em kg: '))
planeta = int(input('Digite o planeta desejado: '))
if planeta == 1:
    print(f'Sua massa em Mercúrio é igual a: {peso * 0.37:.1f}kg')
elif planeta == 2:
    print(f'Sua massa em Vênus é igual a: {peso * 0.88:.1f}kg')
elif planeta == 3:
    print(f'Sua massa em Marte é igual a: {peso * 0.38:.1f}kg')
elif planeta == 4:
    print(f'Sua massa em Júpiter é igual a: {peso * 2.64:.1f}kg')
elif planeta == 5:
    print(f'Sua massa em Saturno é igual a: {peso * 1.15:.1f}kg')
elif planeta == 6:
    print(f'Sua massa em Urano é igual a: {peso * 1.17:.1f}kg')

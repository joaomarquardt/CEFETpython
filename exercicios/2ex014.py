#14) Faça um programa que leia a sigla do estado em que uma pessoa nasceu e imprima uma das mensagens abaixo:
# •carioca
# •paulista
# •mineiro
# •baiano
# •outros casos
estado = str(input('Digite a sigla do estado em que nasceu: ')).strip().upper()
if estado == 'RJ':
    print('• carioca')
elif estado == 'SP':
    print('• paulista')
elif estado == 'MG':
    print('• mineiro')
elif estado == 'BA':
    print('• baiano')
else:
    print('• outros casos')
valor = int(input('Digite um valor: R$'))
notas2 = valor // 2
moeda1 = (valor % 2)
print(f'R${valor}\n'
      f'{notas2} notas de 2\n'
      f'{moeda1} moeda/s de 1')

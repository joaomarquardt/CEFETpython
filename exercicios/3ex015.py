#15) Faça um programa que leia a altura e o sexo (codificado em 1 = masculino e 2 = feminino) de um grupo
# de n pessoas lidas do teclado. Calcule e escreva:
# a) Média da altura dos grupo
# b) Média da altura dos homens
# c) Média da altura das mulheres
# d) Maior altura do grupo
# e) Menor altura do grupo
n = int(input('Digite o número de pessoas a serem registradas: '))
aux = 1
mediaM = mediaF = media = maior = menor = qtdM = qtdF = 0
while aux <= n:
    print(f'===== {aux}ª PESSOA =====')
    altura = float(input('Altura em cm: '))
    sexo = str(input(f'Sexo [M/F]: ')).lower()[0]
    while sexo not in 'mf':
        print('Opção inválida. Tente novamente.')
        sexo = str(input(f'Sexo [M/F]: ')).lower()[0]
    if aux == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        elif altura < menor:
            menor = altura
    if sexo == 'm':
        mediaM += altura
        qtdM += 1
    elif sexo == 'f':
        mediaF += altura
        qtdF += 1
    media += altura
    aux += 1
print(f'Média de altura do grupo: {media / n:.1f}'
      f'\nMédia de altura dos homens: {mediaM / qtdM:.1f}'
      f'\nMédia de altura das mulheres: {mediaF / qtdF:.1f}'
      f'\nMaior altura do grupo: {maior}'
      f'\nMenor altura do grupo: {menor}')

'''1a Questão: Faça um programa que leia uma data no formato dd – mm – aaaa. E em seguida escreva qual será
o próximo dia, mês e ano. Obs.: Verifique todas as possibilidades. Lembre-se que existem anos bissextos. Não permita
que o usuário digite uma data inválida.'''

print('TABELA DE DIAS EM CADA MÊS:'
      '\nJAN: 31    --    JUL: 31'
      '\nFEV: 28/29 --    AGO: 31'
      '\nMAR: 31    --    SET: 30'
      '\nABR: 30    --    OUT: 31'
      '\nMAI: 31    --    NOV: 30'
      '\nJUN: 30    --    DEZ: 31')
print('=-' * 15)
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
dianovo = mesnovo = anonovo = 0
certos = 0
erro = False
if dia < 1 or dia > 31:
    if mes < 1 or mes > 12:
        print('Dia e mês inválidos.')
    else:
        print('Dia inválido. Tente novamente.')
elif mes < 1 or mes > 12:
    if dia < 1 or dia > 31:
        print('Dia e mês inválidos.')
    else:
        print('Mês inválido. Tente novamente.')
else:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia > 31:
            print('Dia inválido. Tente novamente.')
            erro += 1
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print('Dia inválido. Tente novamente.')
            erro += 1
    if erro == 0:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            if mes == 2 and dia >= 30:
                print(f'Não existe dia {dia} em fevereiro. Tente novamente.')
            elif mes == 2 and dia == 29:
                dianovo = 1
                mesnovo = 3
                certos += 1
            elif mes == 2 and dia == 28:
                dianovo = 1
                mesnovo = 3
                certos += 1
            else:
                dianovo = dia + 1
                certos += 1
        else:
            if mes == 2 and dia == 29:
                print(f'Não existe dia 29 em fevereiro em ano NÃO bissexto. Tente novamente.')
            elif mes == 2 and dia == 28:
                dianovo = 1
                mesnovo = 3
                certos += 1
            else:
                dianovo = dia + 1
                certos += 1
        if mes == 2 and dia >= 30:
            print(f'Não existe dia {dia} em fevereiro. Tente novamente.')
        if mes == 12:
            mesnovo = 1
            certos += 1
        else:
            mesnovo = mes + 1
            certos += 1
        anonovo = ano + 1
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia == 31:
                dianovo = 1
                certos += 1
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia == 30:
                dianovo = 1
                certos += 1
if certos >= 2:
    print(f'Data digitada: {dia:0>2}/{mes:0>2}/{ano}'
          f'\nData nova: {dianovo:0>2}/{mesnovo:0>2}/{anonovo}')

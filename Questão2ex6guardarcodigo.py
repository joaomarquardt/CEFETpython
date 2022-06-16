'''def automovel(arquivo1, arquivo2):
    priarq = open(arquivo1, 'w')
    print('\033[31;1;4m--- 1° ARQUIVO ---\033[m')
    priarq.write(input(str(f'Código do carro: ')).strip())
    priarq.write(input(str('Modelo do carro: ')).strip().title())
    segarq = open(arquivo2, 'w')
    print('\033[31;1;4m--- 2° ARQUIVO ---\033[m')
    segarq.write(input(str('Código do carro: ')).strip())
    segarq.write(input(str('Cor do carro: ')).strip().title())
    segarq.write('R$')
    segarq.write(input(str('Preço do carro: R$')).strip())
    segarq.write(input(str('Quantidade disponível para venda: ')).strip())

automovel('arq1.txt', 'arq2.txt')'''

'''from time import sleep

def automovel(arquivo1, arquivo2):
    priarq = open(arquivo1, 'w')
    segarq = open(arquivo2, 'w')
    while True:
        print('\033[31;1m------- 1° ARQUIVO -------\033[m')
        while True:
            cod = str(input('Código do carro: ')).strip()
            esta = False
            for c1 in priarq:
                if cod in c1:
                    esta = True
                    break
            if esta:
                print(f'Código já existente. Tente novamente.')
                sleep(1)
            else:
                break
        priarq.write(str(f'{cod:<6}'))
        while True:
            modelo = str(input('Modelo do carro: ')).strip()
            esta = False
            for c2 in priarq:
                if modelo in c2:
                    esta = True
                    break
            if esta:
                print(f'Modelo já existente. Tente novamente.')
                sleep(1)
            else:
                break
        priarq.write(str(f'{modelo:<18}'))
        priarq.write('\n')
        print('\033[31;1m------- 2° ARQUIVO -------\033[m')
        cod = str(input('Código do carro: ')).strip()
        segarq.write(str(f'{:<6}'))
        cor = str(input('Cor do carro: ')).strip().title()
        segarq.write(str(f'{cor:<10}'))
        segarq.write('R$')
        preco = str(input('Preço do carro: R$')).strip()
        segarq.write(str(f'{preco:<12}'))
        segarq.write(input(str('Quantidade disponível para venda: ')).strip())
        segarq.write('\n')
        continuar = str(input('Deseja continuar? [S/N] '))[0]
        if continuar in 'Nn':
            break
        print('--' * 20)
    priarq.close()
    segarq.close()


automovel('arq1.txt', 'arq2.txt')'''

from time import sleep



def verificar(arquivo1, txt, lista, param):
    while True:
        if len(lista) > 0 and param == 0:
            print(f'Carros adicionados até agora:')
            for c1 in range(len(lista)):
                print(f'Código: {lista[c1][0]} | Modelo: {lista[c1][1]}')
            print('--' * 20)
        var = str(input(f'{txt} do carro: ')).strip()
        esta = False
        if len(lista) > 0:
            for c2 in range(len(lista)):
                if lista[c2][param] == var:
                    esta = True
                    break
            if esta:
                print(f'{txt} já existente. Tente novamente.')
                sleep(1)
            else:
                break
        else:
            break
    return var

def automovel(arquivo1, arquivo2):
    priarq = open(arquivo1, 'w')
    segarq = open(arquivo2, 'w')
    carrosVerificar = []
    dado = []
    while True:
        print('\033[31;1m------- 1° ARQUIVO -------\033[m')
        while True:
            codigo = verificar("arq1.txt", "Código", carrosVerificar, 0).strip()
            modelo = verificar("arq1.txt", "Modelo", carrosVerificar, 1).strip().title()
            priarq.write(str(f'{codigo:<6}'))
            priarq.write(str(f'{modelo:<18}'))
            dado.append(codigo)
            dado.append(modelo)
            carrosVerificar.append(dado[:])
            dado.clear()
            priarq.write('\n')
            continuar = str(input('Deseja continuar? [S/N] '))[0]
            print('\033[33;1m-=\033[m' * 25)
            if continuar in 'Nn':
                break
        print(f'Carros adicionados ao total:')
        for c1 in range(len(carrosVerificar)):
            print(f'Código: {carrosVerificar[c1][0]} | Modelo: {carrosVerificar[c1][1]}')
        print('\033[31;1m------- 2° ARQUIVO -------\033[m')
        while True:
            cod = str(input('Código do carro: ')).strip()
            segarq.write(str(f'{cod:<6}'))
            cor = str(input('Cor do carro: ')).strip().title()
            segarq.write(str(f'{cor:<10}'))
            segarq.write('R$')
            preco = str(input('Preço do carro: R$')).strip()
            segarq.write(str(f'{preco:<11}'))
            segarq.write(input(str('Quantidade disponível para venda: ')).strip())
            segarq.write('\n')
            continuar = str(input('Deseja continuar? [S/N] '))[0]
            if continuar in 'Nn':
                break
            print('\033[33;1m-=\033[m' * 25)
        sair = str(input('Deseja parar de acrescentar informações nos arquivos e sair? [S/N] '))[0]
        if sair in 'Ss':
            break
    priarq.close()
    segarq.close()



automovel('arq1.txt', 'arq2.txt')
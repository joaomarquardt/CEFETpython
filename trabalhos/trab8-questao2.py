'''2a Questão: Faça um programa que crie dois arquivos textos para um revendedor de automóveis. O primeiro chamado
“arq1.txt”, contendo o código do carro e o modelo do carro, e um segundo arquivo chamado “arq2.txt”, contendo o código
do carro, cor, preço e a quantidade disponível para a venda do modelo. Todos os dados serão inseridos pelo usuário. '''

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

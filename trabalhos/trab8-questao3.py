'''3a Questão: Com os dois arquivos criados na questão anterior, faça um programa que simule um sistema para consulta e
vendas de carros. O sistema deve ter o seguinte menu de opções: - Consulta da quantidade disponível de um determinado
modelo de carro. Ex.: Se o usuário escolher essa opção, o programa deverá pedir o modelo do carro; então o usuário
digitará o modelo e em seguida o programa informará o total de veículos disponíveis para a venda daquele modelo. Caso o
modelo não exista, deverá aparecer a mensagem: “modelo inexistente”. Lembre-se que podem existir várias cores para o
mesmo modelo. - Consulta de modelos disponíveis de uma determinada cor e entre uma determinada faixa de preços.
Ex.: Se o usuário escolher essa opção, o programa deverá pedir a cor do carro e a faixa de preço, isto é, o valor mínimo
e o valor máximo de preço que o usuário irá informar. Em seguida o programa irá retornar os nomes dos modelos da cor e
faixa de preços especificados pelo usuário. - Fim de programa. '''

def menu():
    print('[1] CONSULTAR CARROS DISPONÍVEIS')
    print('[2] SAIR DO PROGRAMA')
    while True:
        opcao = int(input('Digite a opção desejada: '))
        if opcao != 1 and opcao != 2:
            print('Opção inválida. Tente novamente.')
        else:
            break
    if opcao == 2:
        return print('ADEUS, AMIGO!')
    print('[1] CONSULTAR QUANTIDADE DISPONÍVEL DE DETERMINADO MODELO')
    print('[2] CONSULTAR MODELOS DISPONÍVEIS DE DETERMINADA COR E FAIXA DE PREÇO')
    while True:
        opcao = int(input('Digite a opção desejada: '))
        if opcao != 1 and opcao != 2:
            print('Opção inválida. Tente novamente.')
        else:
            break
    if opcao == 1:
        return 1
    else:
        return 2

def automoveis(arquivo1, arquivo2):
    priarq = open(arquivo1, 'r')
    segarq = open(arquivo2, 'r')
    codigo = ''
    a = menu()
    if a == 1:
        modelo = input('Digite o modelo do carro desejado: ').strip().title()
        for mod in priarq:
            if modelo in mod:
                print(mod[:4])
                codigo = mod[:4]
        if codigo == '':
            print('Modelo inexistente.')
        else:
            qtdDisponivel = 0
            for linha_um in segarq:
                if linha_um[:4] == codigo:
                    num = linha_um[29:]
                    qtdDisponivel += int(num)
            if qtdDisponivel == 1:
                print(f'Há 1 carro do modelo {modelo} disponível.')
            else:
                print(f'Há {qtdDisponivel} carros do modelo {modelo} disponíveis.')
    elif a == 2:
        lista = []
        dado = []
        cor = input('Digite a preferência quanto a cor: ').strip().title()
        valmin = int(input('Valor mínimo: R$'))
        valmax = int(input('Valor máximo: R$'))
        for linha_dois in segarq:
            transformInt = linha_dois[18:28].replace(',', '.').strip()
            transformInt = float(transformInt)
            if linha_dois[6:16].strip() == cor and valmin <= transformInt <= valmax:
                valorcarro = transformInt
                codigo = linha_dois[:4]
                for linha_tres in priarq:
                    if codigo == linha_tres[:4]:
                        nomecarro = linha_tres[6:].strip()
                        dado.append(nomecarro)
                        dado.append(valorcarro)
                        lista.append(dado[:])
                        break
            dado.clear()
        if len(lista) == 0:
            print('Não há nenhum carro disponível com essas especificações.')
        else:
            if len(lista) == 1:
                print(f'Foi encontrado apenas 1 carro com essas características:')
            else:
                print(f'Foram encontrados {len(lista)} carros com essas características:')
            for c in range(len(lista)):
                print(f'{lista[c][0]} - R${lista[c][1]:.0f},00')


print('--' * 20)
print(f'{"BEM VINDO AO CEFET AUTOMOVEIS!":^40}')
print('--' * 20)
automoveis('arq1.txt', 'arq2.txt')

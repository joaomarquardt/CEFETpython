'''2a Questão: Um marciano chegou a uma floresta e se escondeu atrás de uma das 100 árvores quando viu um caçador.
O caçador só tinha cinco balas em sua espingarda. Cada vez que ele atirava, e não acertava, é claro, o marciano dizia:
'estou mais à direita ou mais à esquerda'.
Se o caçador não conseguir acertar o marciano, ele será levado para marte. Implemente esse jogo para dois jogadores,
onde um escolhe a árvore em que o marciano irá se esconder, e o outro tenta acertar. Obs.: Não permita,
em hipótese alguma, que seja escolhida uma árvore fora do intervalo entre 1 e 100. '''

from time import sleep
print('-=' * 20,
      f'\n\033[33;4;1m{"DESCUBRA AONDE O MARCIANO ESTÁ!":^40}\033[m')
print('-=' * 20)
sleep(1)
print('JOGO PARA 2 JOGADORES!')
print('CONCEITO: '
      '\nO jogador 1 será o marciano e escolherá em que árvore o marciano deve se esconder.'
      '\nO jogador 2 será o caçador e escolherá em que árvore atirar.'
      '\nO caçador terá 5 balas em sua espingarda. Caso não acerte nas 5 tentativas disponíveis, o marciano'
      '\nserá levado de volta para Marte.')
print('-=' * 20)
sleep(1)
tentativas = 0
acertou = False
jog1 = int(input('\033[31;1mJOGADOR 1: Escolha aonde o marciano irá se esconder [1 a 100]:\033[m '))
if 1 <= jog1 <= 100:
    jog2 = int(input('\033[35;1mJOGADOR 2: Escolha aonde o caçador atirará [1 a 100]:\033[m '))
    if 1 <= jog2 <= 100:
        print(f'O caçador atirou na árvore {jog2} e...', end=' ')
        tentativas += 1
        sleep(2)
        if jog2 == jog1:
            print('ACERTOU!')
            acertou = True
        else:
            print('ERROU!')
            if jog1 < jog2:
                print("O outro caçador diz: 'Ele está mais para a \033[33mESQUERDA!\033[m'")
            elif jog1 > jog2:
                print("O outro caçador diz: 'Ele está mais para a \033[33mDIREITA!\033[m'")
            print('O caçador agora só tem 4 chances.')
            jog2 = int(input('\033[35;1mJOGADOR 2: Escolha aonde o caçador atirará [1 a 100]:\033[m '))
            if 1 <= jog2 <= 100:
                print(f'O caçador atirou na árvore {jog2} e...', end=' ')
                tentativas += 1
                sleep(2)
                if jog2 == jog1:
                    print('ACERTOU!')
                    acertou = True
                else:
                    print('ERROU!')
                    if jog1 < jog2:
                        print("O outro caçador diz: 'Ele está mais para a \033[33mESQUERDA!\033[m'")
                    elif jog1 > jog2:
                        print("O outro caçador diz: 'Ele está mais para a \033[33mDIREITA!\033[m'")
                    print('O caçador agora só tem 3 chances.')
                    jog2 = int(input('\033[35;1mJOGADOR 2: Escolha aonde o caçador atirará [1 a 100]:\033[m '))
                    if 1 <= jog2 <= 100:
                        print(f'O caçador atirou na árvore {jog2} e...', end=' ')
                        tentativas += 1
                        sleep(2)
                        if jog2 == jog1:
                            print('ACERTOU!')
                            acertou = True
                        else:
                            print('ERROU!')
                            if jog1 < jog2:
                                print("O outro caçador diz: 'Ele está mais para a \033[33mESQUERDA!\033[m'")
                            elif jog1 > jog2:
                                print("O outro caçador diz: 'Ele está mais para a \033[33mDIREITA!\033[m'")
                            print('O caçador agora só tem 2 chances.')
                            jog2 = int(input('\033[35;1mJOGADOR 2: Escolha aonde o caçador atirará [1 a 100]:\033[m '))
                            if 1 <= jog2 <= 100:
                                print(f'O caçador atirou na árvore {jog2} e...', end=' ')
                                tentativas += 1
                                sleep(2)
                                if jog2 == jog1:
                                    print('ACERTOU!')
                                    acertou = True
                                else:
                                    print('ERROU!')
                                    if jog1 < jog2:
                                        print("O outro caçador diz: 'Ele está mais para a \033[33mESQUERDA!\033[m'")
                                    elif jog1 > jog2:
                                        print("O outro caçador diz: 'Ele está mais para a \033[33mDIREITA!\033[m'")
                                    print('O caçador agora só tem 1 chance. Acerte. \033[4mÉ AGORA OU NUNCA!\033[m')
                                    jog2 = int(input('\033[35;1mJOGADOR 2: Escolha aonde o caçador atirará '
                                                     '[1 a 100]:\033[m '))
                                    if 1 <= jog2 <= 100:
                                        print(f'O caçador atirou na árvore {jog2} e...', end=' ')
                                        tentativas += 1
                                        sleep(2)
                                        if jog2 == jog1:
                                            print('ACERTOU!')
                                            acertou = True
                                        else:
                                            print('ERROU!')
                                            print('O caçador errou todas as tentativas. O marciano voltará para sua '
                                                  'terra!')
                                    else:
                                        print('Opção inválida. Tente novamente.')
                            else:
                                print('Opção inválida. Tente novamente.')
                    else:
                        print('Opção inválida. Tente novamente.')
            else:
                print('Opção inválida. Tente novamente.')
    else:
        print('Opção inválida. Tente novamente.')
else:
    print('Opção inválida. Tente novamente.')
if acertou == False:
    print('\033[41mVITÓRIA DO JOGADOR 1!!\33[m')
else:
    if tentativas == 1:
        print('O caçador só precisou de 1 única tentativa para acertar! Parabéns!')
    elif 1 < tentativas < 5:
        print(f'O caçador precisou de {tentativas} tentativas para acertar.')
    else:
        print(f'O caçador precisou de 5 tentativas para acertar. Foi por pouco!')
    print('\033[45mVITÓRIA DO JOGADOR 2!!\33[m')

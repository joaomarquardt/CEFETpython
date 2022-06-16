#8) Faça um programa que peça para o usuário entrar com uma senha e diga se a senha está correta ou incorreta.
# A senha é definida como uma constante pelo programador.
senha = 'batatinhafrita123'
n = str(input('Digite a senha: '))
if n == senha:
    print('Senha correta!')
else:
    print('Senha incorreta!')

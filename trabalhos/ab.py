from datetime import date
ano = int(input('Digite um ano para saber se ele é bissexto ou não. Digite 0 para saber se o SEU ano\n é bissexto. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
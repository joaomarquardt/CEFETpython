segundo = int(input('Segundos: '))
horas = segundo // 3600
minutos = segundo % 3600 // 60
segundos = segundo % 60
print(f'Total de horas: {horas}\n'
      f'Total de minutos: {minutos}\n'
      f'Total de segundos: {segundos}')

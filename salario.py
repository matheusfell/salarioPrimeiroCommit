print ('Olá, esse simples programa calcula pra você quanto você recebe por hora trabalhada :)')
salario = float(input('Quanto você recebe por mês ?'))
horas = int(input('Quantas horas trabalha por mês ?'))
valor = salario / horas
print ('O valor que você recebe por hora é {:.2f}'.format(valor))
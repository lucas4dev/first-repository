R = float(input())
n = 3.14159

A = n * R * R  # formula da area do circulo

A = ("{:.4f}".format(A))  # tira o "," dos numeros float e também limita a 4 casas decimais apos o ponto
print(f'A={A}')

#  forma simplificada
#  print('A={:.4f}'.format(A))

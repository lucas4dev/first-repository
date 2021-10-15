import math as mt

R = float(input())
pi = 3.14159
fator = (4 / 3.0)

VOLUME = fator * pi * mt.pow(R, 3)  # mt.pow realiza a potenciacao (R*R*R)
print(f'VOLUME = {VOLUME:.3f}')


cod1, quantidade1, precodeum1 = input().split(" ")  # recebe os 3 valores como string na mesma linha
cod2, quantidade2, precodeum2 = input().split(" ")

#  converte as strings para os tipos que precisamos para resolver o problema
cod1 = int(cod1)
cod2 = int(cod2)
quantidade1 = int(quantidade1)
quantidade2 = int(quantidade2)
precodeum1 = float(precodeum1)
precodeum2 = float(precodeum2)

total1 = (quantidade1*precodeum1)
total2 = (quantidade2*precodeum2)

totalfinal = total1 + total2
print(f'VALOR A PAGAR: R$ {totalfinal:.2f}')


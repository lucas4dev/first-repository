nome = input()
salariomensal = float(input())
vendas = float(input())

bonus = vendas * (15/100)
salariototal = salariomensal + bonus
print(f'TOTAL = R$ {salariototal:.2f}')
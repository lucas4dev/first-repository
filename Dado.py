from random import randint

print("Você gostaria de jogar o dado?")
print("Digite s para sim ou n para não")

decisao = input()

while(decisao != 's' and decisao != 'n'):
    print("Por favor, digite um dos 2 caracteres n ou s ")
    decisao = input()

while (decisao == 's'):
        x= randint(1,6)
        print(f'Seu numero é {x}')
        print("Você gostaria de jogar novamente?")
        print("Digite s para sim ou n para não")
        decisao = input()
        if (decisao != 's'):
            print("Por favor, digite um dos 2 caracteres n ou s ")
            decisao = input()

            if(decisao == 'n'):
                print("Fim do programa, volte sempre!")
                quit()


while (decisao == 'n'):
        print("Fim do programa, volte sempre!")
        quit()

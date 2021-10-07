from random import randint

print("Você gostaria de jogar o dado?")
print("Digite s para sim ou n para não")

decisao = input()

while(decisao != 's' and decisao != 'n'):
    print("Por favor, digite um dos 2 caracteres n ou s ")
    decisao = input()

while (decisao == 's'):
        x= randint(1,6)
        
        if(x==1): x = "⚀"
        elif(x==2): x="⚁"
        elif(x==3): x="⚂"
        elif(x==4): x="⚃"
        elif(x==5): x="⚄"
        elif(x==6): x="⚅"
        
        print(f'Seu numero é {x}')
        print("Você gostaria de jogar novamente?")
        print("Digite s para sim ou n para não")
        decisao = input()
        if (decisao != 's' and decisao != 'n'):
            print("Por favor, digite um dos 2 caracteres n ou s ")
            decisao = input()

            if(decisao == 'n'):
                print("Fim do programa, volte sempre!")
                quit()


while (decisao == 'n'):
        print("Fim do programa, volte sempre!")
        quit()

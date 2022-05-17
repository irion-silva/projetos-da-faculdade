''' 3) Criar um programa em python que efetue o calculo de juros simples ou composto'''

continua = True

while continua:
    char_continua = " "
    operacao = str(input("Digite [1] - para Juros Simples ou\nDigite [2] - para Juros Compostos:"))

    if operacao == "1":
        capital = float(input("Informe o valor capital: "))
        tempo = int(input("Informe o período de tempo[Em mêses]: "))
        taxa = float(input("Informe o valor da taxa de juros[Porcentagem]: "))

        while capital < 0 or tempo < 0 or taxa < 0:
            print("Entrada inválida.\nEntre com os valores novamente")
            capital = float(input("Informe o valor capital: "))
            tempo = int(input("Informe o período de tempo[Em mêses]: "))
            taxa = float(input("Informe o valor da taxa de juros[Porcentagem]: "))

        juros = capital * (taxa/100) * tempo

        print("Valor do Juros Simples:R$",juros)
    elif operacao == "2":
        montante = float(input("Informe o valor do montante: "))
        capital = float(input("Informe o valor do capital: "))

        juros = montante - capital

        print("Valor do Juros Compostos:R$", juros)
    else:
        print("Opção inválida")

    while char_continua != "S" and char_continua != "N":
        char_continua = str(input("Deseja continuar[S~N]:"))
        if char_continua == "S":
            continua = True
        elif char_continua == "N":
            continua = False
            break
        else:
            print("Entrada inválida.")
    

''' 2) Fazer um programa em python que receba 4 notas, efetue a média simples, se média >=6 mostre "Aprovado" caso contrario mostre "Reprovado"'''

continua = True

while continua:
    char_continua = " "
    nota1 = float(input("Informe o valor da 1ª nota: "))
    nota2 = float(input("Informe o valor da 2ª nota: "))
    nota3 = float(input("Informe o valor da 3ª nota: "))
    nota4 = float(input("Informe o valor da 4ª nota: "))

    while nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10 or nota4 < 0 or nota4 > 10:
        print("Entrada inválida.\nInforme notas de 0 à 10")
        nota1 = float(input("Informe o valor da 1ª nota: "))
        nota2 = float(input("Informe o valor da 2ª nota: "))
        nota3 = float(input("Informe o valor da 3ª nota: "))
        nota4 = float(input("Informe o valor da 4ª nota: "))

    media = (nota1+nota2+nota3+nota4)/4

    if media >= 6:
        print("Aprovado, com média: ", media)
    else:
        print("Reprovado, com média: ", media)

    while char_continua != "S" and char_continua != "N":
        char_continua = str(input("Deseja continuar?[S~N]:"))
        
        if char_continua == "S":
            continua = True
        elif char_continua == "N":
            continua = False
            break
        else:
            print("Informe uma opção válida")
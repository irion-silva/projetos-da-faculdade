''' 1) Criar um programa em python para resolver qualquer tabuada. Mostre os 10 primeiros resultados'''

continua = True

while continua:
    contador = 1
    char_continua = " "
    tabuada = int(input("Informe o valor inteiro da tabuada que você deseja saber[1~10]:"))

    while tabuada < 0 or tabuada > 10:
        tabuada = int(input("Tabuada fora do intervalo.\nInforme o valor inteiro da tabuada que você deseja saber[1~10]:")) 
    
    while contador <= 10:
        print(tabuada, "x", contador, "=", tabuada*contador)
        contador += 1

    while char_continua != "S" and char_continua != "N":
        char_continua = str(input("Deseja continuar?[S~N]:"))
        
        if char_continua == "S":
            continua = True
        elif char_continua == "N":
            continua = False
            break
        else:
            print("Informe uma opção válido.")
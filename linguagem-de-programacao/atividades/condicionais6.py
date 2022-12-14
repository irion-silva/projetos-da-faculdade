# 1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
import sys

letra = str(input("Informe uma letra: "))
tam = len(letra)

while (tam > 1 or letra.isnumeric()):
        if(letra.isnumeric()):
            print(letra, "não é uma letra") 
        letra = str(input("Informe apenas uma letra: "))
        tam = len(letra)
       
if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'
or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
    print(letra, "é uma vogal")
else:
    print(letra, "é uma consoante")

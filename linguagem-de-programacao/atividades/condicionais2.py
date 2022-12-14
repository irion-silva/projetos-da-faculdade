#2 - Escreva um programa que leia um nome e verifique se este nome é igual ao seu.Imprimir conforme o caso: “NOME CORRETO” ou “NOME INCORRETO”.

nome = str(input("Digite um nome: "))
meunome = "Irion"
if nome == meunome:
    print("Nome correto!")
else:
    print("Nome incorreto!")

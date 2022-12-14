#1 - Faça um programa que receba dois numeros e mostre qual deles é o maior

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

if n1 > n2:
    maior = n1
    menor = n2
    print("Maior número: ", maior)
elif n1 == n2:
    print("Os números são iguais")
else:
    maior = n2
    menor = n1
    print("Maior número: ", maior)
#3 -Fazer um programa que leia a capacidade de um elevador e o peso de 5 pessoas.Informar se o elevador está liberado para subir ou se excedeu a carga máxima.

capacidade = float(input("Informe a capacidade do elevador: "))
pessoa1 = float(input("Digite seu peso: "))
pessoa2 = float(input("Digite seu peso: "))
pessoa3 = float(input("Digite seu peso: "))
pessoa4 = float(input("Digite seu peso: "))
pessoa5 = float(input("Digite seu peso: "))

total_peso = (pessoa1 + pessoa2 + pessoa3 + pessoa4 + pessoa5)

if total_peso <= capacidade:
    print("Liberado para subir")
else:
    print("Excedeu a capacidade máxima!")
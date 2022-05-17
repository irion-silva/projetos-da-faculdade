''' 4) Criar um programa em python que calcule o INSS de um determinado valor'''

salario = float(input("Informe o seu salário: "))
if salario < 1212.0:
    faixa = 1212.0 * 0.075
    print("Contribuição: ", salario + faixa, "/por mês")
elif salario >= 1212.0 and salario <= 2427.35:
    faixa = 1212.0 * 0.075
    faixa2 = (salario - 1212.0) * 0.09
    desconto = faixa + faixa2
    print("O valor será de R$: ", faixa, " + ", faixa2, " = ", faixa+faixa2, "/por mês")
elif salario >= 2427.36 and salario <= 3641.03:
    faixa = 1212.0 * 0.075
    faixa2 = (2427.35 - 1212.0) * 0.09
    faixa3 = (salario - 2427.35) * 0.12
    desconto = faixa + faixa2 + faixa3
    print("O valor será de R$: ", faixa, " + ", faixa2, " + ", faixa3, " = ", faixa + faixa2 + faixa3, "/por mês")
elif salario >= 3641.04 and salario <= 7087.22:
    faixa = 1212.0 * 0.075
    faixa2 = (2427.35 - 1212.0) * 0.09
    faixa3 = (3641.03 - 2427.36) * 0.12
    faixa4 = (salario - 3641.03) * 0.14
    desconto = faixa + faixa2 + faixa3 + faixa4
    print("O valor será de R$: ", faixa, " + ", faixa2, " + ", faixa3, " + ", faixa4, " = ", faixa + faixa2 + faixa3 + faixa4, "/por mês")


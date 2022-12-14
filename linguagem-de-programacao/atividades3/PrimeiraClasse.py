class PrimeiraClasse:
    nome = None

    def imprimir_mensagem(self):
        print("Olá seja bem vindo!")

objeto1 = PrimeiraClasse()
objeto1.nome = "Aluno 1"

print(objeto1.nome)
objeto1.imprimir_mensagem()
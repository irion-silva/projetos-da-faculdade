class FuncionarioTecnico:
    def __init__(self, status):
        self.status = status
    

func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')
 
print(func1.status)
print(func2.status)
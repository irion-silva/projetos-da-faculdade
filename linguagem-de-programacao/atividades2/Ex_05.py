'''5) Construir um programa em Python que simule um cartão de ponto
Regras:
a) Batida inicial não pode ser maior que batida de saída do almoço
b) Batida volta do almoço não pode ser maior que batida saída do almoço
c) Batida volta do almoço não pode ser maior que batida saída
d) mostrar as 4 batidas'''

import datetime
funcionarios = int(input("Informe quantos funcionários bateram ponto: "))

contador = 1
for contador in range(1, funcionarios + 1):
    dt_entrada = input("Informe o horário de entrada do funcionário ao serviço[AAAA-MM-DD HH:MM:SS]")
    dt_entradac = datetime.datetime.strptime(dt_entrada, "%Y-%m-%d %H:%M:%S")
    
    dt_almoco = input("Informe o horário que o funcionário saiu para o almoço[AAAA-MM-DD HH:MM:SS]")
    dt_almococ = datetime.datetime.strptime(dt_almoco, "%Y-%m-%d %H:%M:%S")
    
    dt_volta_almoco = input("Informe o horário que o funcionário voltou do almoço[AAAA-MM-DD HH:MM:SS]")
    dt_volta_almococ = datetime.datetime.strptime(dt_volta_almoco, "%Y-%m-%d %H:%M:%S")
    
    dt_saida = input("Informe o horário que o funcionário saiu do serviço[AAAA-MM-DD HH:MM:SS]")
    dt_saidac = datetime.datetime.strptime(dt_saida, "%Y-%m-%d %H:%M:%S")
       
    while dt_entradac > dt_almococ or dt_almococ > dt_volta_almococ or dt_volta_almococ > dt_saidac:
        print("Entrada inválida")
        dt_entrada = input("Informe o horário de entrada do funcionário ao serviço[AAAA-MM-DD HH-MM-SS]")
        dt_entradac = datetime.datetime.strptime(dt_entrada, "%Y-%m-%d %H:%M:%S")
        
        dt_almoco = input("Informe o horário que o funcionário saiu para o almoço[AAAA-MM-DD HH-MM-SS]")
        dt_almococ = datetime.datetime.strptime(dt_almoco, "%Y-%m-%d %H:%M:%S")
        
        dt_volta_almoco = input("Informe o horário que o funcionário voltou do almoço[AAAA-MM-DD HH-MM-SS]")
        dt_volta_almococ = datetime.datetime.strptime(dt_volta_almoco, "%Y-%m-%d %H:%M:%S")
        
        dt_saida = input("Informe o horário que o funcionário saiu do serviço[AAAA-MM-DD HH-MM-SS]")
        dt_saidac = datetime.datetime.strptime(dt_saida, "%Y-%m-%d %H:%M:%S")
    
    print("Horário de entrada ao serviço do", contador, "ª funcionário:", dt_entradac)
    print("Horário de almoço do", contador, "ª funcionário:", dt_almococ)
    print("Horário de volta do almoço do", contador, "ª funcionário:", dt_volta_almococ)
    print("Horário de saída do serviço do", contador, "ª funcionário:", dt_saidac)
    



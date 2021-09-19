#Entrada
tempo_servico = float(input("Digite o tempo de serviço: "))
bonus_anual = float(input("Digite o valor do bônus em R$: "))

#Processamento
bonificacao = tempo_servico * bonus_anual

#Saída
print("O valor da bonificação anual é de R$: " "%.2f" % bonificacao)

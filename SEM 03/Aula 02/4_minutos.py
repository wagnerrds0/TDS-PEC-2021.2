#Entrada
minutos = int(input("Digite a quantidade de minutos:"))

#Processamento
horas = minutos // 60
minutos = minutos % 60

#Saída
print(f"{minutos} minuto(s) é igual a {horas} hora(s) e {minutos} minuto(s)")


#Entrada
raio = float(input("Digite o raio:"))

#Processamento
comprimento_circunferencia = 2 * 3.141592 * raio
area_circulo = 3.141592 * raio ** 2 
area_esfera = 4 * 3.141592 * raio ** 2
volume_esfera = 4/3 * 3.141592 * raio ** 3

#Saída
print("Comprimento da Circunferência:" "%.6f" % comprimento_circunferencia)
print("Área do Círculo: " "%.6f" % area_circulo)
print("Área da Esfera: " "%.6f" % area_esfera)
print("Volume da Esfera: " "%.6f" % volume_esfera)

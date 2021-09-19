#Entrada
dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))

#Processamento
resultado = dividendo // divisor
resto = dividendo % divisor

#Saída
print(f"O resultado da divisão inteira entre {dividendo} e {divisor} é: " "%.4f" % resultado)
print("O resto é:" "%.4f" % resto)

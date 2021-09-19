#Entrada
preco_produto = float(input("Digite o valor do produto:"))

#Processamento
desconto = preco_produto * (90/100)
diferenca_produto = preco_produto - desconto

#Saída
print(f"Valor do produto R$: {preco_produto}")
print("Valor do produto com desconto é R$" "%.2f" % desconto)
print(" A diferença foi de R$" "%.2f" % diferenca_produto) 

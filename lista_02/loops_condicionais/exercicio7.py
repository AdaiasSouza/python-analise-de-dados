# Exercício 7 - 
#Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
# adicione à lista, apenas os valores pares e imprima a lista

valor_limite = 20
valor_inicial = 4
list_valor = []

while valor_inicial <= valor_limite:
	if valor_inicial%2 == 0:
		list_valor.append(valor_inicial)
	valor_inicial += 1
print(list_valor)


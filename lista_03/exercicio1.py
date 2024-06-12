# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
list_elementos = [1, 2, 3]
index = 0
for valor in list_elementos:
	valor_potencia = pow(valor, 3)
	list_elementos[index] = valor_potencia
	index += 1
print(list_elementos)

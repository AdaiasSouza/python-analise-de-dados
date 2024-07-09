# Exercício 1 - 
#Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
# e depois faça uma chamada à função para listar os números

def numeros_pares():
	number_pares, number_impares  = [], []
	for number in range(21):	
		if number%2 == 0:
			number_pares.append(number)
		else:
			number_impares.append(number)
	return number_pares

print(numeros_pares())
	



# Exercício 4 - 
#Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def retorna_argumento(arg1, *list_element):
	return arg1

a = 1
b = [1, 2, 3, 4]
print("Passagem de 1: ", retorna_argumento(a))
print("Passagem de lista: ", retorna_argumento(b))

# Exercício 3 - 
#Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def append_value(new_list, var1, var2):
	new_list.append(var1)
	new_list.append(var2)
	return new_list

lista = [1, 2, 3, 4]
print(lista)
print(append_value(lista, 5, 6))
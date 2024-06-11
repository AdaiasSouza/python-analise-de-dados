# Exercício 3 - 
#Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

tupla_valores = (1, 2, 3, 4)
list_valores = []
print(tupla_valores)
for elemento in tupla_valores:	
	value_list = elemento*2
	list_valores.append(value_list)
print(list_valores)
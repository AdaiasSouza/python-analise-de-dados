# Exercício 6 - 
#Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela,
# mas quando for encontrado o valor 23, interrompa a execução do programa

contador = 0
limite = 100
while contador < limite:
	print(contador)
	if contador == 23:
		break
	contador += 1
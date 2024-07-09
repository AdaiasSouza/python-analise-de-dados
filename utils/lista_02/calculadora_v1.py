# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

soma = lambda num_1, num_2: num_1+num_2
subtracao = lambda num_1, num_2: num_1-num_2
multiplicacao = lambda num_1, num_2: num_1*num_2
divisao = lambda num_1, num_2: num_1/num_2

inicia_menu = True
while inicia_menu:	
	print("\n******************* Calculadora em Python *******************")
	print("1 - Soma \n2 - Subtracao \n3 - Multiplicacao \n4 - Divisao")
	opcao_menu = int(input("Seleciona uma opcao: "))

	if opcao_menu in range(1,5,1):
		num_1 = float(input("Informe um numero: "))
		num_2 = float(input("Informe um numero: "))

		opcao_soma, opcao_subt, opcao_mult, opcao_divi = 1, 2, 3, 4

		while opcao_menu == opcao_soma:
			print(f"\t{num_1} + {num_2} = {soma(num_1, num_2)}")
			opcao_menu = str(input("Efetuar nova soma ? S -> Sim N -> Nao: "))
			if opcao_menu.upper() == 'N':
			   opcao_menu = None
		while opcao_menu == opcao_subt:
			print(f"\t{num_1} - {num_2} = {subtracao(num_1, num_2)}")
			opcao_menu = str(input("Efetuar nova subtracao ? S -> Sim N -> Nao: "))
			if opcao_menu.upper() == 'N':
			   opcao_menu = None
		while opcao_menu == opcao_mult:
			print(f"\t{num_1} x {num_2} = {multiplicacao(num_1, num_2)}")
			opcao_menu = str(input("Efetuar nova multiplicacao ? S -> Sim N -> Nao: "))
			if opcao_menu.upper() == 'N':
			   opcao_menu = None
		while opcao_menu == opcao_divi:
			if num_2 != 0:
			   print(f"\t{num_1} / {num_2} = {divisao(num_1, num_2)}")
			else:
			   print(f"Divisao inválida")
			opcao_menu = str(input("Efetuar nova divisao ? S -> Sim N -> Nao: "))
			if opcao_menu.upper() == 'N':
			   opcao_menu = None
	else:
		print("\tOpcao inválida")

	inicia_menu = str(input("\tMenu Principal ? S -> Sim, N -> Não: "))
	if inicia_menu.upper() == 'N':
		inicia_menu = False
	print()
print("Fim da execucao...")
print()


# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10
valor_limite = 5
list_valor = [valor for valor in range(1, 11, 1) if valor < valor_limite]
print(list_valor)
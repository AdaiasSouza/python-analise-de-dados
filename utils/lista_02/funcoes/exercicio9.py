# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]
busca_letra = 'a'
print("Base de palavras: ", palavras)
contem_a = [palavra for palavra in palavras if busca_letra in palavra]
print("Palavras que contem letra a: ", contem_a)

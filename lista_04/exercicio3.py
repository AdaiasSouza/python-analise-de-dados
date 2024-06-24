# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.
class Smartphone():
	"""docstring for Smartphone"""
	def __init__(self, tamanho, interface):		
		self.tamanho = tamanho
		self.interface = interface

class MP3Player(Smartphone):
	super.__init__(tamanho, interface)
	def __init__(self, capacidade):
		self.capacidade = capacidade


mp3 = MP3Player(32)
mp3.tamanho = 4
mp3.interface = 'mobile'
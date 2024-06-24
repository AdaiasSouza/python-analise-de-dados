"""import random"""
from os import system, name


class Game():
    """docstring for Game"""

    def __init__():
        print("Classe Game criada")

    def limpa_tela(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


class GameForca(Game):
    def __init__(self):
        print("Iniciando Jogo da forca!")



gf = GameForca()
gf.limpa_tela()
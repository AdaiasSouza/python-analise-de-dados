"""
 Exercício 2
    Crie uma classe chamada Pessoa() com os atributos:
        nome, cidade, telefone e e-mail.
    Use pelo menos 2  métodos especiais na sua classe.
    Crie um objeto da sua classe
    e faça uma chamada a pelo menos um dos seus métodos
    especiais.
"""


class Pessoa():
    """docstring for Pessoa"""

    def __init__(self, nome, cidade, telefone, e_mail):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.e_mail = e_mail

    def imprime_pessoa(self):

        # print(f"Nome: {self.nome} Cidade: {self.cidade} \
        #             Telefone: {self.telefone} \
        #                 E-mail: {self.e_mail}")
        msg_string = "Nome: {%s}".format(self.nome)
        print(msg_string)

    def troca_telefone(self, novo_telefone):
        fone_antigo = self.telefone
        self.telefone = novo_telefone
        print(f"Mudança de telefone: {fone_antigo} -> {self.telefone}")


# Instanciando Classes
p1 = Pessoa('Kayte', 'Maranguape', '87626262', 'kayte_love@gmail.com')
p1.imprime_pessoa()
p1.troca_telefone('87998877')
p1.imprime_pessoa()
print()
p2 = Pessoa('Amora', 'Fortaleza', '32335566', 'amora_love@gmail.com')
p2.imprime_pessoa()
p2.troca_telefone('34965454')
p2.imprime_pessoa()
print()

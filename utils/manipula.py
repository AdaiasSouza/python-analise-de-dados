import os
import pandas as pd
# data.citychicago.org endereços de datasets

root_path = os.getcwd()
arquivo = open('file_text.txt', 'r')
print(arquivo.read())
# arquivo.write("Escrevendo no arquivo Python")
# arquivo.close()
# arquivo = open('file_text.txt', 'a')
# arquivo.write("\aEscrevendo no arquivo Python mas em outra linha")
arquivo.close()

with open('file_text.txt', 'r') as txt_file:
	
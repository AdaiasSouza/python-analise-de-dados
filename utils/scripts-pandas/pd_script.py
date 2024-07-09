import pandas as pd
import os

diretorio = '/home/adaias-souza/Documentos/'\
            'python/python-analise-de-dados/dataset'
dataset = os.listdir(diretorio)[0]
diretorio_dataset = os.path.join(diretorio, dataset)

# 1. Ler o dataset
df = pd.read_csv(diretorio_dataset, header=0)
print(df.head())
print(df.shape)
'''print(df.columns)'''
'''2. Selecionar colunas'''

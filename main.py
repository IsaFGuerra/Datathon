import pandas as pd
import json
import matplotlib.pyplot as plt


# Abrindo arquivos
caminho_arquivo_temperaturas = "dados/Annual_Surface_Temperature_Change.csv"
with open(caminho_arquivo_temperaturas, 'r') as arquivo:
    # Leia o conteúdo do arquivo
    temperatura = pd.read_csv(arquivo.read())
  
print(temperatura)
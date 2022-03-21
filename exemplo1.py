import pandas as pd
import datetime
import numpy as np

df_1 = pd.read_csv('doc1.txt', encoding='ISO-8859-1', sep = ';')
df_2 = pd.read_csv("doc2.txt", encoding="ISO-8859-1", sep = ";")
df_3 = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/ARQUIVOS TESTE/21055Z1 - 300.txt', encoding='ISO-8859-1', sep = ';')
df_4 = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/ARQUIVOS TESTE/21058N1 - 400.txt', encoding='ISO-8859-1', sep = ';')
df_5 = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/ARQUIVOS TESTE/53325Z2A.1- 500.txt', encoding='ISO-8859-1', sep = ';')
df_6 = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/ARQUIVOS TESTE/53555Z2.2 - 300.txt', encoding='ISO-8859-1', sep = ';')
df_7 = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/ARQUIVOS TESTE/G2460050092.1 - 300.txt', encoding='ISO-8859-1', sep = ';')
df_8 = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/ARQUIVOS TESTE/G2461050092.1 - 250.txt', encoding='ISO-8859-1', sep = ';')
df_9 = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/ARQUIVOS TESTE/G25121644J2.2 - 300.txt', encoding='ISO-8859-1', sep = ';')

from pandas.core.reshape.concat import concat
df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])

#Limpar dados
df.info()
df.set_index(df['Dt Termino'], inplace=True)
df.drop(['Dt Termino'], axis=1, inplace=True)

#Tratando a coluna 'Med Bruta' e criando três colunas no df
lista = []
for item in df['Med Bruta']:
  lista.append(item)
print(lista)

new_lista = []
espessura = []
largura = []
comprimento = []

for a in lista:
    new_lista = a.split('X')
    print(new_lista)
    for i in range(0, len(new_lista)):
        if i == 0:
            espessura.append(new_lista[i])
        elif i == 1:
            largura.append(new_lista[i])
        else:
            comprimento.append(new_lista[i])

print(espessura)
print(largura)
print(comprimento)

df['Espessura'] = espessura
df['Largura'] = largura
df['Comprimento'] = comprimento

df.drop(['Med Bruta'], axis=1, inplace=True)
df.info()
df.head()

#Salvar arquivo em csv
pd.DataFrame(df.to_csv('teste.csv'))


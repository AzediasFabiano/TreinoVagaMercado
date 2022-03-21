import pandas as pd
import datetime

vendas_df = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/Contoso - Vendas  - 2017.csv', sep=';')
clientes_df = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/Contoso - Clientes.csv', sep=';')
produto_df = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/Contoso - Lojas.csv', sep=';')

display(vendas_df[:1])
print(len(vendas_df))
display(clientes_df[:1])
print(len(clientes_df))
display(produto_df[:1])
print(len(produto_df))
display(lojas_df[:1])
print(len(lojas_df))

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produto_df = produto_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]
print(lojas_df)

#Juntar os df selecionados
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
vendas_df = vendas_df.merge(produto_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')

vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail Cliente'})
#vendas_df = vendas_df.rename(columns={'Nome do Produto_x': 'Nome do Produto'})
print(vendas_df[:3])

#Qual cliente comprou mais vezes
frequencia_clientes = vendas_df['E-mail Cliente'].value_counts()
print(frequencia_clientes)

frequencia_clientes[:5].plot(figsize=(15,5))

#Qual loja mais vendeu
vendas_loja = vendas_df.groupby('Nome da Loja').sum().sort_values('Quantidade Vendida', ascending=False)
print(vendas_loja)

vendas_loja = vendas_loja[['Quantidade Vendida']]
print(vendas_loja)

vendas_loja[:5].plot(figsize=(15,10), kind='bar')

maior_valor = vendas_loja['Quantidade Vendida'].max()
melhor_loja = vendas_loja['Quantidade Vendida'].idxmax()
print(melhor_loja, maior_valor)

#Qual produto menos vendeu
menor_valor = vendas_loja['Quantidade Vendida'].min()
pior_loja = vendas_loja['Quantidade Vendida'].idxmax()
print(pior_loja, menor_valor)

#Filtrando informações em porcentagem
qde_vend = vendas_df['Quantidade Vendida'].sum()
qde_dev = vendas_df['Quantidade Devolvida'].sum()
print('{:.2%}'.format(qde_dev / qde_vend))

vendas_lojaTal = vendas_df[vendas_df['ID Loja'] == 306]
qde_vend = vendas_lojaTal['Quantidade Vendida'].sum()
qde_dev = vendas_lojaTal['Quantidade Devolvida'].sum()
print('{:.2%}'.format(qde_dev / qde_vend))

loja = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]

#Modificar df
vendas_df['Data da venda'] = pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')
vendas_df['Ano da venda'] = vendas_df['Data da venda'].dt.year
vendas_df['Mês da venda'] = vendas_df['Data da venda'].dt.month
vendas_df['Dia da venda'] = vendas_df['Data da venda'].dt.day
print(vendas_df)
vendas_df.info()
vendas_df.to_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/arquivoTratado.csv', sep=';', encoding='latin1')
dg = pd.read_csv('/content/drive/MyDrive/2022/Aplicação/TratarDados/arquivoTratado.csv', sep=';', encoding='latin1')
vendas_df['ID Cliente'][45000]
vendas_df[['ID Cliente', 'ID Loja', 'ID Produto']]
vendas_df.info()





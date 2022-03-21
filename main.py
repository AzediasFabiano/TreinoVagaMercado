#Projeto de IA para ativos da bolsa de valores

from http import server
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import login as login
import password as password
import time
from time import sleep
import numpy as np
import pytz






mt5.initialize(server='ICMarketsSC-Demo', login=, password='')
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

''' keys=["Open", "High", "Low", "Close"] candle

# extrair indicador : rsi, media movel

#
#Fazer uma carteira de ativos - coletar os preços de: abretura, alto, baixo e fechamento.
dias = 1000  #maximo historico possivel
timezone = pytz.timezone("Etc/UTC")
data_from = datetime(2020, 1, 10)
data_to = datetime(2022, 2, 12)

#while True:
ticks = mt5.copy_ticks_range('BTCUSD', mt5.TIMEFRAME_M5, data_from, data_to, dias)
x = pd.DataFrame(ticks)
x['time'] = pd.to_datetime(x['time'], unit='s')
print(x.head(10))
    #x.set_index(x['time'], inplace=True)
    #x.drop(['tick_volume', 'spread', 'real_volume'], axis=1, inplace=True)
    #print(pd.DataFrame(x.iloc[-1]).T)
    #pd.DataFrame(x.iloc[-1]).T.to_csv('DF_EURUSD.csv', mode='a', header=False, index=False) #index=False columns=['Propriedade','Valor']
    #time.sleep(1)
'''
    #salvar em arquivo continuamente

while True:
    rates_cota = mt5.copy_rates_from_pos(, mt5.TIMEFRAME_D1, 0, 10)
    data = pd.DataFrame(rates_cota)
    data.set_index(data['time'], inplace=True)  # coloca a coluna time como indice
    data.drop(['time'], axis=1, inplace=True)  # apaga a coluna time
    data['time'] = pd.to_datetime(data['time'], unit='s')
    print('O valor do close é: ', pd.DataFrame(data.iloc[-1]).T) #só os preços fechados print('O valor do close é: ', x['close'].iloc[-1])
    pd.DataFrame(data.iloc[-1]).T.to_csv('DaDOS_PREcOS.csv', mode='a', header=False, index=False)
    time.sleep(1)

mt5.shutdown()

'''
lista = list(x)
coluna = []
for col in lista:
    coluna.append(col)
print(coluna)

#salvar em arquivo continuamente
dias = 100
data = time.time()
while True:
    x = mt5.copy_rates_from('EURUSD', mt5.TIMEFRAME_M5, data, dias)
    x = pd.DataFrame(x)
    x['time'] = pd.to_datetime(x['time'], unit='s')
    print('O valor do close é: ', pd.DataFrame(x.iloc[-1]).T) #só os preços fechados: print('O valor do close é: ', x['close'].iloc[-1])
    pd.DataFrame(x.iloc[-1]).T.to_csv('DaDOS_PREcOS.csv', mode='a', header=False, index=False)
    time.sleep(1)


#d = mt5.terminal_info() #Obtém o estado e os parâmetros do terminal MetaTrader 5 conectado
#d = d._asdict() #transforma em dicionario

# coletar informações detalhadas
ativos = 'EURUSD'
info = mt5.symbol_info(ativos)
dinfo = info._asdict()

#transformar informações de ativos em dataframe , select e visible = true 
df = pd.DataFrame(list(dinfo.items()), columns=['Propriedade','Valor'])
print(df)

for p in dinfo:
    print("{} = {}".format(p, dinfo[p]))

ativos = mt5.symbols_get()
lista = []
for ativo in ativos:
    lista.append(ativo.name)
print(len(lista))

ativo = 'EURUSD'
date = datetime(2021, 1, 2)
flag = mt5.COPY_TICKS_ALL
dados = mt5.copy_ticks_from(ativo, date, 10, flag) #Recebe ticks do terminal MetaTrader 5, a partir da data especificada
df = pd.DataFrame(dados)
print(df)
#df.describe(include='all')

mt5.shutdown()

# plotamos os ticks no gráfico
plt.plot(dados['time'], dados['ask'], 'r-', label='ask')
plt.plot(dados['time'], dados['bid'], 'b-', label='bid')

# exibimos rótulos
plt.legend(loc='upper left')

# adicionamos cabeçalho
plt.title('EURUSD')

# mostramos o gráfico
plt.show()
'''
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.parse
from selenium.webdriver.common.by import By

contatos_df = pd.read_excel('MsgWhatsapp.xlsx')
print(contatos_df)

navegador = webdriver.Chrome(executable_path=r"C:\Users\Usuário\executavel\python install\chromedriver.exe")
navegador.get("https://web.whatsapp.com/")

#len(navegador.find_elements(by=By.CLASS_NAME, value="_3GlyB")) < 1:
while len(navegador.find_elements(by=By.ID, value='side')) < 1:
    sleep(1)

print('passei')
for i, msg in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, 'Pessoa']
    numero = contatos_df.loc[i, 'Numero']
    texto = urllib.parse.quote(f"oi {pessoa}! {msg}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(by=By.ID, value='side')) < 1:
        sleep(1)
    navegador.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    sleep(10)

navegador.close()

print('foi')


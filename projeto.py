# Automação de encaminhamentos de mensagens via whatsapp
# Usando a Funcionalidade nativa do whatsapp de encaminhar mensagem
# Encaminhar de 5 em 5 mensagens
# pip install selenium pyperclip webdriver-manager
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChormeDriverManager
# 
# service = Service(ChormeDriverManager().install())
# nav = webdriver.Chrome(service=service)
# nav.get("https://web.whatsapp.com/")



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com/")
# time.sleep(15555)

mensagem = """ Boa noite!! Estou automatizando algumas mensagens via whatsapp, com o intuito de capar novos clientes de forma automatizada"""
lista_contatos = ["Meu Numero", "testes"]

# enviar mensagem para o Meu Mumero para depois poder encaminhar

# Clicar na lupaS
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys()
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)

# escrever mensagem para nos mesmo
pyperclip.copy(mensagem)
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL+"v")
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').send_keys(Keys.ENTER)
time.sleep(2)






qtds_contatos = len(lista_contatos)

if lista_contatos % 5 == 0:
    qtde_blocos = qtds_contatos / 5
else:
    qtde_blocos = int(qtds_contatos / 5) + 1
    
    for i in range(qtde_blocos):
        # rodar o codigo de encaminhar
        i_inicial = i * 5 
        i_final = (i + 1) * 5 
        lista_enviar = lista_contatos[i_inicial:i_final]
        
        # selecionar a mensagem para enviar e abre a caixa de encaminhar
        lista_elementos = nav.find_elements('class_name','_2AOIt')
for item in lista_elementos:
    mensagem = mensagem.replace("\n","")
    texto = item.replace("\n","")
    if item in texto:
        elemento = item
        break
ActionChains(nav).move_to_element(elemento).perfom()
elemento.find_element('class name','_3u9t-').click()
time.sleep(0.5)
nav.find_element('xpath','//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
nav.find_element('xpath','//*[id="main"]/span[2]/div/button[4]/div').click()
time.sleep(1)

for nome in lista_enviar:
    #seleconar os 5 contatos para enviar
    # escrever o nome do contato
    nav.find_element('xpath','//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2/div/div[1]/p]').send_keys("Meu Numero")
    time.sleep(1)
    # dar ENTER
    nav.find_element('xpath','//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2/div/div[1]/p]').send_keys(Keys.ENTER)
    time.sleep(1)
    # apagar o nome do contato
    nav.find_element('xpath','//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2/div/div[1]/p]').send_keys(Keys.BACKSPACE)
    time.sleep(1)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Instanciando o driver do Chrome e entrando no site
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)
navegador.get('https://docs.google.com/forms/d/e/1FAIpQLSfhkPYL4jX3Ld9ns_bW51LTrB5xCSOvIFRVemowsDZRtDRIwg/viewform')
navegador.maximize_window()

# Marcando as caixas de respostas
navegador.find_element('xpath', '//*[@id="i6"]/div[2]').click()
time.sleep(0.5)
navegador.find_element('xpath', '//*[@id="i16"]/div[3]/div').click()
time.sleep(0.5)

# Enviando o formulário
navegador.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div/span/span').click()
time.sleep(0.5)

# Fechando o navegador
navegador.quit()
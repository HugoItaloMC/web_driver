from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Abrir Navegador
browser = webdriver.Chrome()

# Buscar Web Site
browser.get('https://www.somatematica.com.br/lotofacilResultados.php')

# Pesquisa no "Search Engine"
resultado1 = browser.find_element(By.TAG_NAME, "/html/body/div[5]/div[1]/section/table[1]").get_property('strong')

print(resultado1)

#Lançamento de Horas JumpLabel

import select
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.select import Select


navegador = webdriver.Chrome()
navegador.maximize_window()

navegador.get("http://admin.jumplabel.com.br/#Index")

Login = navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[1]/input')
Login.send_keys('christopher.tominaga@jumplabel.com.br')

Senha = navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[2]/input')
Senha.send_keys('Tominaga2$')

navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[4]/div[1]/button').click()

navegador.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div/div[1]/div/button').click()

time.sleep(3)

Projeto = Select(navegador.find_element_by_xpath('//*[@id="Hour_Id_Project"]'))
Projeto.select_by_visible_text('SAS - Amil')

Descricao = Select(navegador.find_element_by_xpath('//*[@id="Hour_Description"]'))
Descricao.select_by_visible_text('Dia Útil')

Localidade = Select(navegador.find_element_by_xpath('//*[@id="Hour_LocalityId"]'))
Localidade.select_by_value("2")

today = date.today()

d1 = today.strftime("%d/%m/%Y")

Data = navegador.find_element_by_xpath('//*[@id="Hour_Date"]')
Data.send_keys(d1)

Hora_de_entrada = navegador.find_element_by_xpath('//*[@id="Hour_Arrival_Time"]')
Hora_de_entrada.send_keys('09:00')

Hora_almoco = navegador.find_element_by_xpath('//*[@id="Hour_Beginning_Of_The_Break"]')
Hora_almoco.send_keys('12:30')

Hora_volta_almoco = navegador.find_element_by_xpath('//*[@id="Hour_End_Of_The_Break"]')
Hora_volta_almoco.send_keys('13:30')

Hora_de_saida = navegador.find_element_by_xpath('//*[@id="Hour_Exit_Time"]')
Hora_de_saida.send_keys('18:00')

Atividades = navegador.find_element_by_xpath('//*[@id="Hour_Activies"]')
Atividades.send_keys('Análise de Dados')

navegador.find_element_by_xpath('//*[@id="HoursForm"]/div[11]/button[2]').click()


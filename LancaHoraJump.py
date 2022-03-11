#Lançamento de Horas JumpLabel

import select
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.select import Select


navegador = webdriver.Chrome()
navegador.maximize_window()

navegador.get("http://admin.jumplabel.com.br/#Index")

# No email colocar seu email de login
Login = navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[1]/input')
Login.send_keys('email')

# No password colocar sua senha de login
Senha = navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[2]/input')
Senha.send_keys('password')

navegador.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/form/div[4]/div[1]/button').click()

navegador.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div/div[1]/div/button').click()

# O Sleep é em segundos
time.sleep(3)

# No project colocar o nome do projeto que deseja selecionar
Projeto = Select(navegador.find_element_by_xpath('//*[@id="Hour_Id_Project"]'))
Projeto.select_by_visible_text('project')

# Escolhi 'Dia Útil', pelo tipo de lançamento normal
Descricao = Select(navegador.find_element_by_xpath('//*[@id="Hour_Description"]'))
Descricao.select_by_visible_text('Dia Útil')

# O Valor 2 é o 'Remoto', mas colocar no número o valor que deseja
Localidade = Select(navegador.find_element_by_xpath('//*[@id="Hour_LocalityId"]'))
Localidade.select_by_value("2")

today = date.today()

d1 = today.strftime("%d/%m/%Y")

Data = navegador.find_element_by_xpath('//*[@id="Hour_Date"]')
Data.send_keys(d1)

# Alterar o horário conforme desejado
Hora_de_entrada = navegador.find_element_by_xpath('//*[@id="Hour_Arrival_Time"]')
Hora_de_entrada.send_keys('09:00')

# Alterar o horário conforme desejado
Hora_almoco = navegador.find_element_by_xpath('//*[@id="Hour_Beginning_Of_The_Break"]')
Hora_almoco.send_keys('12:30')

# Alterar o horário conforme desejado
Hora_volta_almoco = navegador.find_element_by_xpath('//*[@id="Hour_End_Of_The_Break"]')
Hora_volta_almoco.send_keys('13:30')

# Alterar o horário conforme desejado
Hora_de_saida = navegador.find_element_by_xpath('//*[@id="Hour_Exit_Time"]')
Hora_de_saida.send_keys('18:00')

# Colocar em Activity suas atividades para que sejam descritas no campo de atividades
Atividades = navegador.find_element_by_xpath('//*[@id="Hour_Activies"]')
Atividades.send_keys('Activity')

navegador.find_element_by_xpath('//*[@id="HoursForm"]/div[11]/button[2]').click()


import pyautogui
import time
import pandas
import pyperclip

# Passo 1: Acessar o sistema da empresa

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("opera developer")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)
# Passo 2: Fazer login na empresa

pyautogui.click(x=959, y=403)
pyautogui.write("meu login")

pyautogui.click(x=889, y=466)
pyautogui.write("minha senha")

pyautogui.click(x=943, y=538)

time.sleep(5)
#print(pyautogui.position())

#Passo 3: Baixar a base de dados

pyautogui.click(x=710, y=358)
pyautogui.click(x=757, y=222)
pyautogui.click(x=847, y=590)

time.sleep(5)

#Passo 4: Calcular os indicadores

#importar a base de dados
tabela = pandas.read_csv(r"D:\5_Programação\IntensivaoPython\class\class1\assets\Compras.csv", sep=";")
print(tabela)

#calculo dos indicadores

#total gasto
total_gasto = tabela["ValorFinal"].sum()
#quantidade 
quantidade = tabela["Quantidade"].sum()
#preco medio
preco_medio = total_gasto / quantidade

#Passo 5: Enviar o email para a diretoria/para o chefe

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/nbox")
pyautogui.press("enter")

time.sleep(5)

# clicar em escrever
pyautogui.click(x=139, y=207)

# preencher o email
pyautogui.write("cepldudu@gmail.com")
pyautogui.press("tab") # seleciona o email

pyautogui.press("tab") # passar para o campo assunto
pyperclip.copy("Relatório de compras")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # passar para o campo do corpo do texto

texto = f"""
Prezados,

Segue o relatório de compras,

Total Gasto: R$ {total_gasto:,.2f};
Quantidade de Produtos: {quantidade:,};
Preço Médio: R$ {preco_medio:,.2f};

Qualquer dúvida, é só chamar,
Att.,
Carlão do Caminhão
"""


pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar
pyautogui.hotkey("ctrl", "enter")







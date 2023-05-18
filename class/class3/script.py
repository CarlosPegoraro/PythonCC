# Passo 1: Abrir o navegador

import unicodedata
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

# Passo 2: Importar base de dados
import pandas as pd

tabela = pd.read_excel(r"D:\5_Programação\IntensivaoPython\class\class3\assets\commodities.xlsx")
print(tabela)

# Passo 3: Para cada produto na base de dados

for linha in tabela.index:
    
    produto = tabela.loc[linha, "Produto"]
    
    # entrar no site melhor cambio na pagina do milho
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    link = link.replace("ó", "o").replace("á", "a").replace("ã", "a").replace("ç", "c").replace("ú", "u").replace("é", "e")
    # link = unicodedata.normalize("NFKD", link).encode("ascii", "ignore")
    navegador.get(link)
    
    # Pegar cotacao do milho
# Passo 4: Pegar o preco atual do produto
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    
    #Tratar a informacao, string para number
    cotacao = cotacao.replace(".", "").replace(",", ".")
    cotacao = float(cotacao)
    print(cotacao)

# Passo 5: Atualizar o preco na base de dados
    tabela.loc[linha, "Preço Atual"] = cotacao
    print(tabela)

# Passo 6: Decicdir quais produtor a gente vai comprar
    tabela["Comprar"] = tabela["Preço Atual"] < tabela["Preço Ideal"]

# Passo 7: Exportar a base de dados atualizada
navegador.quit()
tabela.to_excel(f"D:/5_Programação/IntensivaoPython/class/class3/assets/commodities2.xlsx", index=False)


# Passo 1: Importar base de dados
import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r"D:\5_Programação\IntensivaoPython\class\class2\assets\clientes.csv", encoding="latin", sep=";")

# deletar a coluna inutil
# axis = 0 -> deleta linha / axis = 1 -> deleta coluna
tabela = tabela.drop("Unnamed: 8", axis=1)

# Passo 2: Visualizar a base de dados
print(tabela)

# Passo 3: Tratamento de dados
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

tabela = tabela.dropna()

# Passo 4: Analise Inicial = entender como estao as notas dos clientes
print(tabela.describe())

# Passo 5: Analise completa = tracar o perfil ideal de cliente = entender como caca caracteristica impacta a nota
for coluna in tabela.columns:
    # Criacao do grafico
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    # Exibicao do grafico
    grafico.show()
    
#Perfil do cliente:
    # Clientes acima de 10 anos
    # O salário não interfere no perfil
    # Áreas de trabalho: Entreterimento e Artista (evitar construção)
    # Tem entre 10 a 15 anos de experiência
    # Famílias de até 7 pessoas
    
    #Obs Final:
        # O salario mais baixo apresenta uma leve queda no perfil


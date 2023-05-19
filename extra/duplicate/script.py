lista = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]

# Forma simples

# Set e List
meu_set = list(set(lista))
print(meu_set)
# retorna -> [1, 2, 3, 4, 5]

# dict.fromkeys
meu_dict = list(dict.fromkeys(lista))
print(meu_dict)
# retorna -> {5: None, 4: None, 3: None, 2: None, 1: None} / com list -> [5, 4, 3, 2, 1]

# se for um arquivo de codigos

import pandas as pd

produtos = pd.read_csv('D:/5_Programação/IntensivaoPython/extra/duplicate/Produtos.csv', sep=";")
# produtos = produtos.drop_duplicates(keep="last") # remove qualquer valor igual
produtos = produtos.drop_duplicates("Produto") # remove os valores igual na coluna "Produto"
print(produtos)
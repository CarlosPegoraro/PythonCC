# Primeirto codigo - mudar o valor da variavel

# Errado
produto1 = "maca"
produto2 = "pera"

# Certo
produto1, produto2 = produto2, produto1
print(produto1, produto2)

# Segundo Codigo - List comprehension

preco_produtos = {
    "iphone": 5000,
    "ipad": 3000,
    "airpods": 2000,
    "macbook": 15000
}

imposto = []

# Errada
for produto in preco_produtos:
    imposto.append(preco_produtos[produto] * 1)
    
# Certo
imposto = [preco_produtos[produto] * 0.1 for produto in preco_produtos]

# Terceiro Codigo - Ternary operator

vendas = 1000
meta = 500

# Errado
if vendas >= meta:
    bonus = 30
else:
    bonus = 0

# Certo
bonus = 30 if vendas >= meta else 0

# Quarto Codigo - Unpacking

def calcular_imposto(valor):
    ir = 0.2 * valor
    csll = 0.0375 * valor
    iss = 0.05 * valor
    return ir, csll, iss

venda = 1000

# Errado 
impostos = calcular_imposto(venda)
ir = impostos[0]
csll = impostos[1]
iss = impostos[2]

# certo
ir, csll, iss = calcular_imposto(venda)

# Quinto Codigo - Atribuir Multiplos Valores

# Para dados com diferentes objetivos
vendedor = "CArlos"
vendas = 2000
bonus = 30

# Para dados com memso objetivo
meta1, meta2, meta3 = 1000, 2000, 3000

# Sexto COdigo - Transformar String em Numero

# # Para quando vendas pode nao ser usada como numero
# vendas = input("Quanto voce venceu ontem?")
# vendas = float(vendas)

# # Para quando vendas sempre vai ser um numero
vendas = float(input("Quanto voce vendeu ontem?"))
imposto = vendas * 0.1
print(imposto)

# Setimo COdigo - Ler Aquivos

with open("D:/5_Programação/IntensivaoPython/extra/7powercodes/vendas.txt", "r") as arquivo:
    vendas = [float(item.strip()) for item in arquivo.readlines()]
    
print(vendas)










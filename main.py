
import pandas as pd
'''
tabela = pd.read_excel(r'E:\DADOS\Jan-Dez.xlsx')


dados = tabela[['Centro de custo']]


string = "Totais de "

while True:
    input = input("Adicione o numero: ")
    string_nova = string+input
    aux = dados["Centro de custo"].str.startswith(f"{string_nova}")
    resultado = dados.loc[aux]
    print(resultado)
'''

tabela = pd.read_excel(r'E:\DADOS\Jan-Dez.xlsx')

dados = tabela[['Centro de custo']]

string = "Totais de "

while True:
    input_usuario = input("Adicione o numero: ")
    string_nova = string + input_usuario
    aux = dados["Centro de custo"].str.startswith(f"{string_nova}")
    resultado = tabela.loc[aux]
    print(resultado)
    


import pandas as pd 

x = pd.read_excel(r"C:\Users\workstation\Desktop\DADOS\Dados_Rodrigo_Abril.xlsx")

dados = x["Centro de custo"]

print("Tabela: ")

aux = 'Totais de 0'

dados_filtrados = dados.str.startswith('Totais de 01')

novos_dados = dados_filtrados.value_counts()

print(novos_dados)

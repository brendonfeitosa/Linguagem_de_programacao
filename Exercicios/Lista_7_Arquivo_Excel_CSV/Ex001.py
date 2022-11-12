'''1. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente a média da coluna do arquivo 'Valor Unitário'.'''

import pandas as pd
df1 = pd.read_excel('C:/Users/Brendon_Feitosa/OneDrive/Documentos/1. ADS - Fatec/2º Termo - 1º sem. 2022/Linguagem_de_programacao/Exercicios/Lista_7_Arquivo_Excel_CSV/Vendas.xlsx')
cont = 0
total = 0
for i in df1['Valor Unitário']:
    total += i
    cont += 1
media = total / cont
print('O valor médio da coluna (Valor Unitário) é: R$ {:.2f}'.format(media))
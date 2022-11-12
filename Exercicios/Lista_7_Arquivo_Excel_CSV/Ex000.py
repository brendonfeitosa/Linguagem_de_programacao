import pandas as pd

df1 = pd.read_excel('C:/Users/Brendon_Feitosa/OneDrive/Documentos/1. ADS - Fatec/2º Termo - 1º sem. 2022/Linguagem_de_programacao/Exercicios/Lista_7_Arquivo_Excel_CSV/Vendas.xlsx')
print(df1)

print('\n------------------------------------------\n')
df2 = pd.read_csv('C:/Users/Brendon_Feitosa/OneDrive/Documentos/1. ADS - Fatec/2º Termo - 1º sem. 2022/Linguagem_de_programacao/Exercicios/Lista_7_Arquivo_Excel_CSV/Propaganda.csv')
print(df2)
print('\n------------------------------------------\n')
df2.info()
print(df1['ID Loja'].value_counts())

import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Brendon_Feitosa/OneDrive/Documentos/1. ADS - Fatec/2º Termo - 1º sem. 2022/Linguagem_de_programacao/Exercicios/Lista_7_Arquivo_Excel_CSV/Propaganda.csv')
plt.hist(df['Radio'], 5, rwidth=0.8, color = 'orange')
plt.title('Propaganda Via Rádio')
plt.xlabel('Custo')
plt.ylabel('Frequência Absoluta')
plt.show()

#para usar o len, vou usar o len(df2['ID Loja'])
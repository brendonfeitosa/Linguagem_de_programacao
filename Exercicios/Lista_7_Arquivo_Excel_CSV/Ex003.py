'''3. Crie um programa que carregue o arquivo Vendas.xlsx, por meio da biblioteca Pandas. Calcule e apresente o valor máximo da coluna do arquivo 'Valor Final'.'''

import pandas as pd
df1 = pd.read_excel('Vendas.xlsx')
maximo = max(df1['Valor Final'])
print('O valor máximo da coluna (Valor final) é: R$ {}'.format(maximo))

'''4. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Calcule e apresente o valor máximo da coluna do arquivo 'Jornal'.'''

import pandas as pd
df1 = pd.read_csv('Propaganda.csv')
maximo = max(df1['Jornal'])
print('O valor máximo da coluna (Jornal) é de: R$ {}'.format(maximo))

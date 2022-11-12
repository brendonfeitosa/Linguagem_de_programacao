'''6. Crie um programa que carregue o arquivo Propaganda.csv, por meio da biblioteca Pandas. Gere um histograma, referente a coluna TV, utilizando a biblioteca Matplotlib, apresente na cor verde.'''

import pandas as pd
df1 = pd.read_csv('Propaganda.csv')
#print(df1)
print()
import matplotlib.pyplot as plt
df2 = pd.read_csv('Propaganda.csv')
plt.hist(df2['TV'], 5, rwidth = 0.8, color = 'green')
plt.title('Coluna TV')
plt.xlabel('Custo')
plt.ylabel('Frequência absoluta')
plt.show()

'''3. (Função sem retorno com parâmetro) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.'''

def resultado(subtracao):
  print('O resultado da subtração é:',subtracao)

def calcular():
  n1 = float(input('Digite um número: '))
  n2 = float(input('Digite um número: '))
  subt = n1 - n2
  resultado(subt)

def main():
  calcular()
main()
'''5. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.'''

def calculo(novo_preco):
  print(f'O novo preço do produto é: R$ {novo_preco:.2f}')

def calcular():
  preco = float(input('Digite o preço do produto: R$ '))
  porcentagem = float(input('Digite o percentual (%) para reajuste: '))
  reajuste = preco + (preco * porcentagem / 100)
  calculo(reajuste)

def main():
  calcular()
main()
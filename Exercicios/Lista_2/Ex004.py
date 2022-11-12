'''4. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.'''

def reajustar(p): # p é um parâmetro que esta recebendo uma cópia do valor que esta na variável preço na main()
  novo_preco = p + (p * 9 / 100)
  print(f'O novo preço é R$ {novo_preco:.2f}')

def main():
  preco = float(input('Digite o preço do produto: '))
  reajustar(preco) # preço é um argumento
main()
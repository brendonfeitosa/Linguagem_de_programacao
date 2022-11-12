'''5. (Função sem retorno sem parâmetro) Faça uma função/método que receba o preço antigo e atual de um produto, determine o percentual de acréscimo entre esses valores e apresente-o.'''

def aumento():
  preco_antigo = float(input('Digite o preço antigo: R$ '))
  preco_atual = float(input('Digite o preço atual: R$ '))

  acrescimo = ((preco_atual - preco_antigo) / preco_antigo) * 100

  print(f'O acréscimo percentual é: {acrescimo:.2f} %')

def main():
  aumento()
main()
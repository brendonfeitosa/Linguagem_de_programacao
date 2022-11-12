'''10. (Função sem retorno com parâmetro) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.'''

def verificacao(n):
  if n == 'Ana' or n == 'ana':
    return True
  else:
    return False

def main():
  nome = input('Digite um nome: ')
  m = verificacao(nome)
  print(m)
main()
'''7. (Função sem retorno com parâmetro) Faça uma função/método para calcular a tabuada de um número informado pelo usuário. Crie outra função que calcule a tabuada de um intervalo, por exemplo realize as taduabas do 3 ao 8. Aqui deverá ocorrer para as duas funções, PASSAGEM DE PARÂMETRO POR VALOR.'''

def tabuada(v1):
  for i in range(1,11):
    multiplicacao = v1 * i
    print(v1, 'x', i, '=', multiplicacao)

  print('\n')

def funcao2(vl1, vl2):
  for i in range(vl1+1, vl2):
    for j in range(1, 11):
      multiplicacao = i * j
      print(i, 'x', j, '=', multiplicacao)

    print('\n')

def main():
  n1 = int(input('Digite um número inteiro: '))
  n2 = int(input('Digite um número inteiro: '))
  tabuada(n1)
  funcao2(n1, n2)
main()
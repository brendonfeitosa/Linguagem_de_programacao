'''2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.'''

def calculo():
  n1 = float(input('Digite um número: '))
  n2 = float(input('Digite um número: '))
  subtracao = n1 - n2
  return subtracao

def main():
  print('O resultado da subtração é: ',calculo())
main()

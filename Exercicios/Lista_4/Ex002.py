'''2. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.'''

def somar(n1,n2):
  soma = n1 + n2
  print('A soma entre os números {} e {} é {}'.format(n1,n2,soma))

def main():
  numero1 = int(input('Digite um número inteiro: '))
  numero2 = int(input('Digite um número inteiro: '))
  somar(numero1,numero2)
main()

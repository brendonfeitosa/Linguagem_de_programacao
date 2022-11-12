'''9. (Função sem retorno com parâmetro) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.'''

def numero(valor):
  if valor % 2 == 0:
    print(' \n O número é par')
  else:
    print('\n O número é impar')

def par_impar():
  num = int(input('Digite um número inteiro: '))
  numero(num)

def main():
  par_impar()
main()
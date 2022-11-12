'''6. (Função sem retorno com parâmetro) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. Não use vetor. Aqui deverá ocorrer para as duas variáveis, PASSAGEM DE PARÂMETRO POR VALOR.'''

def acumulo(valor_inicial , valor_final):
  soma = 0
  if valor_inicial >= 0 and valor_final >= 0:
    if valor_inicial > valor_final:
      while valor_inicial > valor_final:
        soma += valor_final
        valor_final += 1
      soma += valor_inicial

    elif valor_final > valor_inicial:
      while valor_final > valor_inicial:
        soma = soma + valor_inicial
        valor_inicial += 1
      soma += valor_final

    elif valor_inicial == valor_final:
      soma = valor_inicial

  print('A soma dos números é:',soma)

def main():
  x = int(input('Digite o valor inicial (digite um valor inteiro): '))
  y = int(input('Digite o valor final (digite um valor inteiro): '))
  acumulo(x , y)
main()
'''3. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.'''

def calculo(percent,salario):
  novo_salario = (percent / 100 * salario) + salario
  print('O novo salário é: R$',novo_salario)

def main():
  salario_atual = float(input('Digite o salário atual: R$ '))
  percentual_aumento = float(input('Digite o percentual para aumento do salário: '))
  calculo(percentual_aumento,salario_atual)
main()
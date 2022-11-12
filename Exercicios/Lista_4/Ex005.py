'''5. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.'''

def calcular_aumento(porcentagem,salario):
  novo_salario = salario + (salario * porcentagem / 100)
  return novo_salario

def main():
  total_novo_salario = 0
  total_salario_antigo = 0
  porcent = float(input('Informe a porcentagem: '))
  for i in range(4): #vou chamar 4 vezes a função
    salari = float(input('Informe o salário: R$ '))
    total_salario_antigo = total_salario_antigo + salari
    total_novo_salario = total_novo_salario + calcular_aumento(porcent,salari)
  print('Total após o aumento  é R$',total_novo_salario)
  diferenca = total_novo_salario - total_salario_antigo
  print('A diferença é: R$',diferenca)
main()

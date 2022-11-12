'''3. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2.'''

def triangulo():
  base = int(input('Digite a base do triângulo: '))
  altura = int(input('Digite a altura do triângulo: '))
  area = (base * altura) / 2
  return area

def main():
  valor_area = triangulo()
  print('A área do triângulo é: ',valor_area)
main()
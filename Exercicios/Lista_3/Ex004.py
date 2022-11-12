'''4. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado².'''

def quadrado():
  lado = int(input('Digite a medida do lado do quadrado: '))
  area_quadrado = lado * lado
  return area_quadrado

def main():
  print('A área do quadrado é: ',quadrado())
main()

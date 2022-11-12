'''3. (Função sem retorno sem parâmetro) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. O valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. Não pode usar vetor e função pronta da linguagem Python.'''

def divisiveis():
  a = int(input('Digite um número inteiro: '))
  b = int(input('Digite um número inteiro: '))
  c = int(input('Digite um número inteiro: '))
  cont = 0
  while b <= c:
    if b % a == 0:
      print('O número',b ,' é divisivel por',a)
      cont += 1
    b += 1
  print('A quantidade de números divisiveis é:',cont)

def main():
  divisiveis()
main()
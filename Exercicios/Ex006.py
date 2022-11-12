#6. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação

def tabuada():
  num = int(input('Digite um número inteiro : '))
  i = 1
  while i <= num:
    x = 1
    y = i
    while x <= i:
      print(y, end = '\t')
      y += i
      x += 1
    print()
    i += 1

def main():
  tabuada()
main()


# Para ter a mesma forma de apresentação use assim o print(r, end = '\t')
'''6. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne/mostre o valor bool True para par e False para ímpar.'''

#return True
#return False
#devo usar if e else

def verificar():
  n = int(input('Digite um número: '))
  if n % 2 == 0:
    return True # sempre que tiver return a lógica é encerrada, não devemos fazer nada depois desta função.
  else:
    return False

def main():
  print('O número é par? ',verificar())
main()
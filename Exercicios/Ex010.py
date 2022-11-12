'''10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
Observvação: Não pode usar vetor e função pronta da linguagem Python.'''

# Digite seu código aqui.

# S = 1 + 1 + 1/2! + 1/3 + 1/4!
# S = 1 + 1 + 0.5 + 0.16 + 0.041
# S = 2.66 + 0.041
# 3! = 3 * 2 * 1 = 6
# 4! = 1 * 2 * 3 * 4 = 24    1/4!   1/24  = 0.041

# N = int(input('Informe o valor de N termos: '))

# S = 1

def fatorial():
  n = int(input('Digite um número inteiro: '))
  contador = soma = f = x = 1
  while contador <= n:
    while x <= contador:
      f *= x
      x += 1
    print(1/f)
    soma += (1/f)
    contador += 1
  print(f'A soma é igual a: {soma:.2f}')

def main():
  fatorial()
main()
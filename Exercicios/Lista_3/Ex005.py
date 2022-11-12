'''5. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.'''

def numero():
  num = int(input('Digite um número inteiro: '))
  if num % 2 == 0:
    return True
  else:
    return False
  
def main():
  if numero() == True:
    print('É par')
  else:
    print('É impar')
main()

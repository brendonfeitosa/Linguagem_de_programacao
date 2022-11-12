'''12. Faça uma função/método para verificar uma senha, contando/apresentando quantos dígitos numéricos e quantas letras existem. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.'''

def verificar(senha):
  quantidade_letras = 0
  quantidade_numeros = 0
  for i in range(len(senha)):
    if senha[i].isalpha() == True:
      quantidade_letras = quantidade_letras + 1
    elif senha[i].isdecimal() == True:
      quantidade_numeros += 1
  print('A quantidade de letras é:',quantidade_letras)
  print('A quantidade de números é:',quantidade_numeros)

def main():
  digitar_senha = input('Digite uma senha sem espaços e caracteres especiais: ')
  verificar(digitar_senha)
main()

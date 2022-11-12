#Outra fora de fazer o ex013

def verificar_senha(senha):
  quantidade_letras = 0
  quantidade_numeros = 0
  quantidade_carac_especial = 0
  for i in range(len(senha)):
    if senha[i].isalpha() == True:
      quantidade_letras = quantidade_letras + 1
    elif senha[i].isdecimal() == True:
      quantidade_numeros += 1
    elif not senha[i].isdecimal or not senha[i].isalpha == True:
      quantidade_carac_especial += 1

  print('A quantidade de letras é:',quantidade_letras)
  print('A quantidade de números é:',quantidade_numeros)
  print('A quantidade de números é:',quantidade_carac_especial)

def main():
  print('Crie uma senha seguindo os seguintes parametros:\n 2 primeiros caracteres números;\n 1 caractere especial;\n 5 letras')
  digitar_senha = input('Digite uma senha: ')
  verificar_senha(digitar_senha)
main()
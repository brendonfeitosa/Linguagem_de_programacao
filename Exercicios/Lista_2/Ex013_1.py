'''13. Uma senha deve ser criada a partir da seguinte regra:
Dois primeiros números
Um caracter especial
Cinco letras
Faça uma função/método para verificar esta senha esta correta ou não, use FATIAMENTO DE STR Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.'''

def verificar_senha(senha):
  q_letras = 0
  q_numeros = 0
  q_especial = 0

  if (senha[:2].isdecimal()) == True:
    if (senha[2].isdecimal()) == False and (senha[2].isdecimal()) == False:
      if (senha[3:].isalpha()) == True:
        if len(senha[3:]) >= 5:
          print('A senha {} esta correta' .format(senha))
        else:
          print('A senha deve conter pelo menos 5 letras')
      else:
        print('A senha esta incorreta')
    else:
      print('A senha deve conter um caracter especial')
  else:
    print('A senha deve inciar por 2 números')

def main():
  print('Crie uma senha seguindo os seguintes parametros:\n 2 primeiros caracteres números;\n 1 caractere especial;\n 5 letras')
  digitar_senha = input('Digite uma senha: ')
  verificar_senha(digitar_senha)
main()
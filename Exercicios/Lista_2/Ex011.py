'''11. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras a tem numa frase. Não use NENHUMA função pronta da linguagem Python. Aqui deverá ocorrer, PASSAGEM DE PARÂMETRO POR VALOR.'''

def verificacao(texto):
  #removendo os espaços e a pontuação do texto e deixando o texto em letras minusculas.
  texto = texto.lower()
  texto = texto.replace(' ','')
  texto = texto.replace('\n','')
  texto = texto.replace('!','')
  texto = texto.replace('?','')
  texto = texto.replace(',','')
  texto = texto.replace(';','')
  texto = texto.replace('.','')

  #podemos usar 'texto = texto.replace()' para remover acentuação
  #removendo acentuação da letra A
  texto = texto.replace('á','a')
  texto = texto.replace('ã','a')
  texto = texto.replace('à','a')

  contador_a = 0
  for caracteres in texto:
    if caracteres == 'a':
      contador_a += 1
  print('A quantidade de letras (A) no texto é:',contador_a)

def main():
  digitacao = input('Digite uma frase: ')
  verificacao(digitacao)
main()
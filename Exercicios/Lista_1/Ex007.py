'''7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.
N1, N2 e N3 são notas.

P1, P2 e P3 são pesos.

Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)'''

def notas():
  letra = input('Digite a letra para efetuar o cálculo - A (média aritimética) P (média ponderada): ')
  nota1 = float(input('Digite a 1ª (primeira) nota: '))
  nota2 = float(input('Digite a 2ª (segunda) nota: '))
  nota3 = float(input('Digite a 3ª (terceira) nota: '))

  if letra == 'A' or letra == 'a':
    media = (nota1 + nota2 + nota3) / 3
    print(f'A média aritimética do aluno é: {media:.2f}')
  elif letra == 'P' or letra == 'p':
    media_ponderada = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5+3+2)
    print(f'A média ponderada do aluno é: {media_ponderada:.2f}')

def main():
  notas()
main()
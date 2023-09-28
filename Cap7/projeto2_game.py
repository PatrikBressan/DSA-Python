'''Pseudocódigo:
1) Definir uma lista de palavras possíveis;
2) Escolher uma palavra aleatória da lista;
3) Criar uma lista vazia para armazenar as letras adivinhadas;
4) Criar uma lista vazia para armazenar as letras erradas;
5) Definir o número máximo de tentativas permitidas;
6) Enquanto o número de tentativas não atingir o limite máximo:
    a) mostrar a palavra como uma série de underscores, com as letras adivinhadas
       preenchidas nos espaços corretos;
    b) pedir ao jogador que adivinhe uma letra;
    c) verificar se a letra adivinhada está na palavra;
    d) se a letra adivinhada está na palavra, adicionar a letra à lista de letras
       adivinhadas e atualizar a exibição da palavra;
    e) se a letra adivinhada não etá na palavra, reduzir o número de tentativas
       restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: nº" e
       exibir a lista de letras erradas atualizadas;
    f) Verificar se todas as letras da palavra foram adivinhadas;
    g) Se todas as letras foram adivinhadas, exibir a mensagem "Você venceu!"
    h) Se o número de tentativas restantes chegar a zero, exibir a mensagem
       "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo.
'''
# Imports
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
   # Windows
   if name == 'nt':
      _ = system('cls')
    
   # Mac ou Linux
   else:
      _ = system('clear')

# Função que desenha a forca na tela
def display_hangman(chances):
   # Lista de estágios da forca
   stages = [
            # Stage 6 - final
            '''
                -------------
                |           |
                |           O
                |          \\|/
                |           |
                |          / \\
                |
                |
                -
            ''',
            # Stage 5
            '''
                -------------
                |           |
                |           O
                |          \\|/
                |           |
                |          /
                |
                |
                -
            ''',
            # Stage 4
            '''
                -------------
                |           |
                |           O
                |          \\|/
                |           |
                |
                |
                -
            ''',
            # Stage 3
            '''
                -------------
                |           |
                |           O
                |          \\|
                |           |
                |
                -
            ''',
            # Stage 2
            '''
                -------------
                |           |
                |           O
                |           |
                |           |
                |
                -
            ''',
            # Stage 1
            '''
                -------------
                |           |
                |           O
                |
                |
                |
                -
            ''',
            # Stage 0
            '''
                -------------
                |           |
                |
                |
                |
                |
                -
            '''
   ]
   return stages[chances]

def game():
   limpa_tela()
   print('\nBem-vindo(a) ao Jogo da Forca!')
   print('Advinhe a palavra abaixo:\n')

   #Lista de palavras para o jogo
   palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'maçã']

   # Escolhe randomicamente uma palavra
   palavra = random.choice(palavras)

   # List comprehension
   letras_descobertas = ['_' for letra in palavra]

   # Nº de chances
   chances = 6

   # Lista para as letras erradas
   letras_erradas = []

   while chances >= 0:
      # Print
      print(display_hangman(chances))
      print(" ".join(letras_descobertas))
      print('\nChances restantes: ', chances)
      print('Letras erradas: ', " ".join(letras_erradas))

      # Tentativa
      tentativa = input('\nDigite uma letra: ').lower()

      # Condicional
      if tentativa in palavra:
         index = 0
         for letra in palavra:
            if tentativa == letra:
               letras_descobertas[index] = letra
            index +=1
      else:
         chances -= 1
         letras_erradas.append(tentativa)
      
      # Condicional
      if "_" not in letras_descobertas:
         print('\nVocê venceu, a palavra era: ', palavra)
         break
   # Fim While
   
   if "_" in letras_descobertas:
      print('\nVocê perdeu, a palavra era: ', palavra)
# Fim def game

# Bloco main
if __name__ == "__main__":
   game()
   print('\nParabéns. Você está aprendendo programação em Python. ;)\n')
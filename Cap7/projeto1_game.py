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
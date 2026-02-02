tabuleiro = [" ", " ", " ",
            " ", " ", " ",
            " ", " ", " "]
def mostrar_tabuleiro(tab):

    print(  ' 1 | 2 | 3' )
    print(f" {tab[0]} | {tab[1]} | {tab[2]} " "A") 
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} " "B")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} " "C")
    print()

def posicao_para_indice(posicao_texto):
    mapa = {
        'A1': 0, 'A2': 1, 'A3': 2,
        'B1': 3, 'B2': 4, 'B3': 5,
        'C1': 6, 'C2': 7, 'C3': 8
    }

    posicao_texto = posicao_texto.upper()

    if posicao_texto in mapa:
        return mapa[posicao_texto]
    else:
        return None

def indice_para_posicao(indice):
    mapa = {
        0: 'A1', 1: 'A2', 2: 'A3',
        3: 'B1', 4: 'B2', 5: 'B3',
        6: 'C1', 7: 'C2', 8: 'C3'
    }
    return mapa[indice]


def pedir_jogada(tab, jogador):
    while True:
        entrada = input(f"Jogador {jogador}, digite a posição (ex: A1, B2): ")

        indice = posicao_para_indice(entrada)

        if indice is None:
            print("Posição inválida. Use A1, A2, B1, etc.")
            continue

        if tab[indice] != " ":
            print("Essa casa já está ocupada.")
            continue

        return indice

def verificar_vencedor(tab):
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in combinacoes:
        if tab[a] == tab[b] == tab[c] and tab[a] != " ":
            return tab[a]

    return None

import random

def jogada_chatgpt(tab):
    livres = []

    for i in range(9):
        if tab[i] == " ":
            livres.append(i)

    if not livres:
        return None

    indice = random.choice(livres)
    posicao = indice_para_posicao(indice)

    print(f"ChatGPT escolheu: {posicao}")

    return indice


jogador = "X"

while True:
    mostrar_tabuleiro(tabuleiro)

    if jogador == "X":
        indice = pedir_jogada(tabuleiro, jogador)
    else:
        indice = jogada_chatgpt(tabuleiro)

    tabuleiro[indice] = jogador

    vencedor = verificar_vencedor(tabuleiro)
    if vencedor:
        mostrar_tabuleiro(tabuleiro)
        print(f"Jogador {vencedor} venceu!")
        break

    if " " not in tabuleiro:
        mostrar_tabuleiro(tabuleiro)
        print("Empate!")
        break

    jogador = "O" if jogador == "X" else "X"


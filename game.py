import json
from random import choice
from os import system, name

def limpar_tela():
    if name == 'nt':
        _ =system('cls')
        
#lendo o arquivo
def game():
    limpar_tela()
    print("------------JOGO DA FORCA------------")
    print()

    # Tente abrir o arquivo JSON e carregá-lo
    try:
        with open('filmes.json', 'r') as arquivo:
            leitura = json.load(arquivo)
        limpar_tela()
    except FileNotFoundError:
        print("Arquivo 'filmes.json' não encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo 'filmes.json'. Verifique o formato do arquivo.")
        return

    #fazendo uma escolha aleatoria de filme
    filme = choice(leitura)
    
    #inserindo _ de letras
    letras_certas = [' ' if letra == ' ' else '_' for letra in filme]
    
    print(' '.join(letras_certas))
    chances = len(filme)
    letras_erradas = []
    
    while chances>0:
        try:    
            print(f"O filme tem {chances} letras")
            tentativa = str(input("Dgite uma letra: ")).lower()
            while tentativa in letras_erradas:
                print("Você já tentou essa letra, tente novamente")
                tentativa = str(input("Dgite uma letra: ")).lower()
            if tentativa not in filme.lower():
                letras_erradas.append(tentativa)
                chances-=1
            else:
                for i, letra in enumerate(filme.lower()):
                    if letra == tentativa:
                        letras_certas[i]=tentativa
            print(' '.join(letras_certas))
            print(f"\nletras erradas: {', '.join(letras_erradas)}")
            print(f"Você tem {chances} chances restantes")
            if "_" not in letras_certas:
                print(f"\nParabens você acertou o filme: {filme}")
                break
        except (ValueError, TypeError):
            print("\nERRO")
            print("Digite Apenas LETRAS")
            continue
    else:
        print("\nque pena, você perdeu")
        print(f"O filme era: {filme}")
            
# Executando o jogo
if __name__ == "__main__":
    game()
    print("\nJogo encerrado.")
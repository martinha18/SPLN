import sys

#Usar flag para tirar espaços em branco
def remove_linhas_repetidas(fonte):
    linhas_vistas = set()
    for linha in fonte:
        if linha not in linhas_vistas:
            sys.stdout.write(linha)
            linhas_vistas.add(linha)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as arquivo:
            remove_linhas_repetidas(arquivo)
    else:
        remove_linhas_repetidas(sys.stdin)


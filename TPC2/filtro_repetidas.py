#!/usr/bin/env python3
'''
Repetidas - Remove linhas repetidas de um programa.

Usage - 
    repetidas options file*

Options
    -s      assume spaces in the beginning or the end of the line make it different
    -e      remove empty lines
    -c      comment lines instead of removing them
'''
from jjcli import *

#Usar flag para tirar espaços em branco, parágrafos...
def remove_linhas_repetidas(cl):
    linhas_vistas = set()
    linhas_vistas.add("")
    linhas_vistas.add("\n")
    
    for linha in cl.input():
        if "-s" not in cl.opt:
            ln = linha.strip()
        else:
            ln = linha

        if ((not ln or ln == "\n") and "-e" not in cl.opt) or ln not in linhas_vistas:
            print(linha, end="")
            linhas_vistas.add(ln)
        else:
            if "-c" in cl.opt:
                print("#", linha, end="")

    print("Linhas vistas: ", linhas_vistas)

def main():
    cl = clfilter(opt="sec", man=__doc__, autostrip=False)
    remove_linhas_repetidas(cl)

if __name__ == "__main__":
    main()

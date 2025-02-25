import re
from jjcli import *
from collections import Counter
from itertools import islice
import json

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def counter(tokens):
    return Counter(*tokens)

def frequencia_relativa(contagem_tokens):
    total_tokens = sum(contagem_tokens.values())
    if total_tokens == 0:
        return {token: 0 for token in contagem_tokens}
    return {token: contagem / total_tokens *1000000 for token, contagem in contagem_tokens.items()}

def pretty_print(freq, relative_freq, opt):
    if "-r" in opt:
        dict_1 = relative_freq
    else:
        dict_1 = freq

    if "-m" in opt:
        new_dict = dict(islice(dict_1.items(), int(opt["-m"])))
    else:
        new_dict = dict_1

    if "-j" in opt:
        try:
            with open("out.json", "w", encoding="utf-8") as arquivo:
                json.dump(new_dict, arquivo, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")
    else:
        print("\n\nToken        Frequency\n")
        for token, count in new_dict.items():
            print(f'{token}:\t\t{count:.2f}')

def ratio(rf1, rf2):
    result = {}
    for key, value in rf1.items():
        if key in rf2:
            result[key] = value / rf2[key]
        else:
            result[key] = 0
    return result


def main():
    """
    Options:
      -r: relative frequency
      -m 500: top 500
      -j: output in json
    """
    cl = clfilter("rm:j", doc=main.__doc__) #documentation is main documentation
    tokens = []

    # lexer
    for txt in cl.text():
        l = lexer(txt)
        tokens.append(l)

    # counter with absolute frequency
    c = counter(tokens)

    # relative frequency
    relative_freq = frequencia_relativa(c)

    # save the results
    pretty_print(c, relative_freq, cl.opt)

if __name__ == "__main__":
    main()
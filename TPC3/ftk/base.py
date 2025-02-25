import re
from jjcli import *
from collections import Counter

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def counter(tokens):
    return Counter(*tokens)

def main():
    cl = clfilter()
    tokens = []
    for txt in cl.text():
        l = lexer(txt)
        #print(l)
        tokens.append(l)
    c = counter(tokens)
    print(c)
    return c
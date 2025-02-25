"""
def total(contagem_tokens):
    total = sum(contagem_tokens.values())
    print(total)
    return total


def frequencia_relativa(contagem_tokens):
    total_tokens = total(contagem_tokens.values())
    if total_tokens == 0:
        result = {token: 0 for token in contagem_tokens}
    result = {token: contagem / total_tokens for token, contagem in contagem_tokens.items()}
    print(result)
    return result
"""

import subprocess
import ast
import sys

def calcular_frequencia_relativa(contagem_tokens):
    """
    Calcula a frequência relativa de cada token com base na contagem fornecida.
    
    :param contagem_tokens: dicionário {token: contagem}
    :return: dicionário {token: frequência relativa}
    """
    total_tokens = sum(contagem_tokens.values())
    if total_tokens == 0:
        return {token: 0 for token in contagem_tokens}
    
    return {token: contagem / total_tokens for token, contagem in contagem_tokens.items()}

def exibir_resultados(contagem_tokens, frequencias):
    """
    Exibe a contagem de tokens e suas frequências relativas.
    """
    print("Contagem de tokens:", contagem_tokens)
    print("Frequências relativas:", frequencias)

def main():
    arquivo = sys.argv[1] if len(sys.argv) > 1 else None
    
    comando = ["ftk-occ"]
    if arquivo:
        comando.append(arquivo)
    
    resultado = subprocess.run(comando, capture_output=True, text=True)
    if resultado.returncode != 0:
        print("Erro ao executar ftk-occ:", resultado.stderr)
        return
    
    try:
        contagem_tokens = ast.literal_eval(resultado.stdout.strip())
        if not isinstance(contagem_tokens, dict):
            raise ValueError
    except (SyntaxError, ValueError):
        print("Erro ao processar a saída do ftk-occ.")
        return
    
    frequencias = calcular_frequencia_relativa(contagem_tokens)
    exibir_resultados(contagem_tokens, frequencias)


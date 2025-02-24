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

# TPC4: Limpar ficheiro corpus e comparar com outro em Português 

## 2025-02-25

## Autor

- PG55983
- Marta Sofia Matos Castela Queirós Gonçalves

## Resumo

#### Limpar ficheiro

Eliminar elementos que aparecem 2 ou menos vezes (ficando apenas com 503909 entradas no dicionário)

-> geralmente correspondem a erros ortográficos ou palavras muito pouco utilizadas

#### Comparar ficheiro com corpus

Pôr a funcionar main_surprise

```
python3 base.py -r -j /home/marta/Desktop/Marta/SPLN/Aula1/tetum-Dicionario_de_fundamentos_elementares_da.txt
python3 compare_pt.py frequency.json > ratio.json
```


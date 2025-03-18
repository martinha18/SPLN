# TPC5: Dicionário PT-TT, Domain Specific Language

## 2025-02-25

## Autor

- PG55983
- Marta Sofia Matos Castela Queirós Gonçalves

## Resumo


## Extra
Sistema de reestrita textual

```
defr a(t)
    the -> o
    cat -> gato
    (\w+) =e=> lambda x: dicionario.get(x[1],x[1])
```

```
def transform_a(t)
    re.sub(r'\bthe\b', 'o', t)
    re.sub(r'\cat\b', 'gato', t)
    re.sub(r'\w+\b', lambda x: dicionario.get(x[1],x[1]), t)
    return t
```
import sys
import json

def get_ratio(our_dict, corpus):
    result = {}
    for word, count in our_dict.items():
        if word in corpus:
            result[word] = count / corpus[word]
        else:
            result[word] = 0
    return result

def read_json(source=None):
    try:
        if source:
            with open(source, "r", encoding="utf-8") as f:
                return json.load(f)
        else: 
            json_texto = input("Write in JSON: ")
            return json.loads(json_texto)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Erro ao processar JSON: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) > 1:
        arquivo_json = sys.argv[1]
        data = read_json(arquivo_json)
    else:
        data = read_json()

    corpus = read_json("./corpus/corpus.json")

    ratio = get_ratio(data, corpus)

    print(json.dumps(ratio, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
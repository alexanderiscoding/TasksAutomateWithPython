#python MergeJsonInExistFile.py example.json example_all.json
import json
import sys

try:
    with open(sys.argv[2], encoding="utf-8") as file_destino:
        destino = json.loads(file_destino.read())
        with open(sys.argv[1], encoding="utf-8") as file_origem:
            try:
                origem = json.loads(file_origem.read())
                with open(sys.argv[2], 'w', encoding='utf8') as outfile:
                        json.dump({**destino, **origem}, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
            except json.decoder.JSONDecodeError:
                print("O arquivo de origem pode não ser um .json")
except FileNotFoundError:
    with open(sys.argv[1], encoding="utf-8") as file:
        origem = json.loads(file.read())
        with open(sys.argv[2], 'w', encoding='utf8') as outfile:
            json.dump(origem, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
except json.decoder.JSONDecodeError:
        print("O arquivo de destino pode não ser um .json")
except Exception as e:
    print("Ocorreu um erro:\n", e)

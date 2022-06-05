#python MergeAllJsonKeyOnlyFile.py id example1.json example2.json... infinite files in only file
import json
import sys

filename = sys.argv[1].rsplit('.', 1)[0]
convertedfilename = "%s_merged_all.json" % (filename)
try:
    with open(convertedfilename) as file:
        print("Já existe um arquivo de destino, favor renomear ou apagar.")
except FileNotFoundError:
    all_files = sys.argv[2:]
    for item in all_files:
        try:
            with open(convertedfilename, encoding="utf-8") as file:
                data_all = json.loads(file.read())
                with open(item, encoding="utf-8") as file:
                    data = json.loads(file.read())
                    jsonData = data[sys.argv[1]]
                    with open(convertedfilename, 'w', encoding='utf8') as outfile:
                        json.dump({**data_all, **jsonData}, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
        except FileNotFoundError:
            with open(item, encoding="utf-8") as file:
                data = json.loads(file.read())
                jsonData = data[sys.argv[1]]
                with open(convertedfilename, 'w', encoding='utf8') as outfile:
                        json.dump(jsonData, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
        except json.decoder.JSONDecodeError:
            print("O arquivo %s pode não ser um .json" % item)
        except Exception as e:
            print("Ocorreu um erro:\n", e)
except Exception as e:
    print("Ocorreu um erro:\n", e)

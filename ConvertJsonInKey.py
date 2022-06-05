#python ConvertJsonInKey.py id example.json
import json
import sys

with open(sys.argv[2], encoding="utf-8") as file:
    try:
        data = json.loads(file.read())
        items = {}
        filename = sys.argv[2].rsplit('.', 1)[0]
        convertedfilename = "%s_converted.json" % (filename)
        items[data[sys.argv[1]]] = data
        with open(convertedfilename, 'w', encoding='utf8') as outfile:
            json.dump(items, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
    except json.decoder.JSONDecodeError:
        print("Esse arquivo pode não ser um .json")

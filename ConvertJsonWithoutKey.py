#python ConvertJsonWithoutKey.py id example.json
import json
import sys

with open(sys.argv[2], encoding="utf-8") as file:
    try:
        data = json.loads(file.read())
        count=0
        items = {}
        filename = sys.argv[2].rsplit('.', 1)[0]
        convertedfilename = "%s_converted.json" % (filename)
        for item in data:
            items[item[sys.argv[1]]] = data[count]
            count +=1
        with open(convertedfilename, 'w', encoding='utf8') as outfile:
            json.dump(items, outfile, sort_keys = True, indent = 4, ensure_ascii = False)
    except json.decoder.JSONDecodeError:
        print("Esse arquivo pode não ser um .json")

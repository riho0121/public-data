import json

files = ["katakana_layer1.json", "katakana_layer2.json", "katakana_layer3.json"]

for f in files:
    with open(f, encoding="utf-8") as fp:
        data = json.load(fp)

    data.sort(key=lambda x: len(x["difficult_word"]), reverse=True)

    with open(f, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)

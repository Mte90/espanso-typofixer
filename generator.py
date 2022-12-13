#!/usr/bin/env python3

from pathlib import Path
from json import load
from collections import OrderedDict
import os
import yaml
import re

file = Path("./words").glob("*.json")
counter = {
    "en": {"words": 0, "typos": 0},
    "fr": {"words": 0, "typos": 0},
    "it": {"words": 0, "typos": 0},
    "es": {"words": 0, "typos": 0},
}
for filename in file:
    if os.path.isfile(filename):
        with open(filename, "r", encoding='utf-8') as f:
            print("Parsing " + str(filename) + " language")
            lang = os.path.splitext(os.path.basename(filename))
            lang = lang[0]
            json = load(f, object_hook=OrderedDict)
            yaml_content = {
                "name": "typofixer-" + lang,
                "parent": "default",
                "matches": [],
            }
            counter[lang]["words"] = len(json.items())
            for (correct_word, misspelled_words) in json.items():
                for misspelled_word in misspelled_words:
                    yaml_content["matches"].append(
                        {
                            "trigger": misspelled_word,
                            "replace": correct_word,
                            "propagate_case": True,
                            "word": True,
                        }
                    )
                counter[lang]["typos"] += len(misspelled_words)
            with open("typofixer-" + lang + "/package.yml", "w", encoding='utf-8') as yaml_file:
                yaml.dump(yaml_content, yaml_file, sort_keys=False, allow_unicode=True)

print("Finished")
print(counter)

with open("./readme.md", "r") as f:
    readme = f.read()
    for lang in counter:
        readme = re.sub(
            "<!--" + lang + "-words-->.*<!--" + lang + "-words-end-->",
            "<!--" + lang + "-words-->" + str(counter[lang]["words"]) + "<!--" + lang + "-words-end-->",
            readme,
        )
        readme = re.sub(
            "<!--" + lang + "-typos-->.*<!--" + lang + "-typos-end-->",
            "<!--" + lang + "-typos-->" + str(counter[lang]["typos"]) + "<!--" + lang + "-typos-end-->",
            readme,
        )

with open("./readme.md", "w") as writer:
    writer.write(readme)

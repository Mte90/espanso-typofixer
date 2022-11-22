#!/usr/bin/env python3

from pathlib import Path
from json import load
from collections import OrderedDict
import os
import yaml

file = Path("./words").glob("*.json")
for filename in file:
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            print("Parsing " + str(filename) + " language")
            lang = os.path.splitext(os.path.basename(filename))
            lang = lang[0]
            json = load(f, object_hook=OrderedDict)
            yaml_content = {
                "name": "typofixer-" + lang,
                "parent": "default",
                "matches": [],
            }
            for (correct_word, misspelled_words) in json.items():
                yaml_content["matches"].append(
                    [
                        {
                            "trigger": correct_word,
                            "replace": misspelled_words,
                            "propagate_case": "true",
                            "word": "true",
                        }
                    ]
                )
                # for misspelled_word in misspelled_words:
            with open("typofixer-" + lang + "/package.yaml", "w") as yaml_file:
                yaml.dump(yaml_content, yaml_file, sort_keys=False)

print("Finished")

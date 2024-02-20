#!/usr/bin/env python
import requests
import os
from SyntaxAutoFix.utils import open_typo_file, save_typo_data

the3_src = requests.get('https://raw.githubusercontent.com/swaits/thethethe.nvim/main/lua/thethethe/dictionary.lua')

the3_content = the3_src.text
the3_content = the3_content.split("\n")
previous_word = ''

lang_path = os.path.dirname(os.path.realpath(__file__)) + '/../words/en.json'

typo_data = open_typo_file(lang_path)
print("Found %s words in english" % len(typo_data))
before = len(typo_data)

for rule in the3_content:
    if ':' in rule:
        misspelled_word, correct_word = rule.split(':')
        if " " in correct_word:
            continue
        correct_word = correct_word.lower()
        misspelled_word = misspelled_word.lower()
        if correct_word not in typo_data:
            typo_data[correct_word] = [misspelled_word]
        else:
            if misspelled_word not in typo_data[correct_word]:
                typo_data[correct_word].append(misspelled_word)

after = len(typo_data)
print("Found %s words on the3" % str(after - before))

save_typo_data(lang_path, typo_data)

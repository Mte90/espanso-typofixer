import requests
import json
import io
import re

the3_src = requests.get('https://raw.githubusercontent.com/swaits/thethethe.nvim/main/lua/thethethe/dictionary.lua')
the3_src = the3_src.text

the3 = {}
the3_src = the3_src.split("\n")
previous_word = ''

for rule in the3_src:
	if ':' in rule:
		misspelled_word, correct_word = rule.split(':')
		if correct_word != previous_word:
			the3[correct_word] = [misspelled_word]
			previous_word = correct_word
		else:
			the3[correct_word].append(misspelled_word)

the3 = json.dumps(the3, indent=2)
with open('../words/extra/the3.json', 'w', encoding='utf-8') as json_file:
	json_file.write(the3)

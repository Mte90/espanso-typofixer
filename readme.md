# Espanso-Typofixer
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)   

This packages is a porting [SyntaxAutoFix](https://github.com/Mte90/SyntaxAutoFix) in Python that is now 7 years old.  
Just used by me and no one else, in the years got tons of words with various hacktoberfest and by daily gathering of typos in English and Italian.

I preferred to migrate to [Espanso](https://espanso.org) for various reasons:

* I don't have to maintain a project by code, just still gather typos
* Python project require `sudo`
* Python project use like 50mb of ram, espanso instead less
* Opening to a wide more usage to gather more typos

## Status (per last update)

* **English**: *<!--en-words-->4383<!--en-words-end-->* words with *<!--en-typos-->5047<!--en-typos-end-->*  typos
* **French**: *<!--fr-words-->69<!--fr-words-end-->* words with *<!--fr-typos-->70<!--fr-typos-end-->* typos
* **Italian**: *<!--it-words-->1174<!--it-words-end-->* words with *<!--it-typos-->1544<!--it-typos-end-->* typos
* **Spanish**: *<!--es-words-->103<!--es-words-end-->* words with *<!--es-typos-->118<!--es-typos-end-->* typos

## How works

The words list are in the words folder in JSON format, the `generator.py` script generate the `.yml` files for the various languages.

The `tools` folder includes some script to convert a CSV to JSON, remove duplicates, GUI to add new word (all based on SyntaxAutoFix).

## TODO

* Define how to upload the packages for espanso hub

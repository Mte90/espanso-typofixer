# Espanso-Typofixer
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)   

* https://hub.espanso.org/typofixer-en
* https://hub.espanso.org/typofixer-es
* https://hub.espanso.org/typofixer-fr
* https://hub.espanso.org/typofixer-it

## Status (per last update)

* **English**: *<!--en-words-->4383<!--en-words-end-->* words with *<!--en-typos-->5047<!--en-typos-end-->* typos
* **French**: *<!--fr-words-->69<!--fr-words-end-->* words with *<!--fr-typos-->70<!--fr-typos-end-->* typos
* **Italian**: *<!--it-words-->1175<!--it-words-end-->* words with *<!--it-typos-->1545<!--it-typos-end-->* typos
* **Spanish**: *<!--es-words-->103<!--es-words-end-->* words with *<!--es-typos-->118<!--es-typos-end-->* typos

## Story

These packages are a porting [SyntaxAutoFix](https://github.com/Mte90/SyntaxAutoFix) in Python that is now 7 years old.
Just used by me and no one else, in the years got tons of words with various hacktoberfest and by daily gathering of typos in English and Italian.

I preferred to migrate to [Espanso](https://espanso.org) for various reasons:

* I don't have to maintain a project by code, just still gather typos
* Python project require `sudo`
* Python project use like 50mb of ram, espanso instead less
* Opening to a wide more usage to gather more typos
* Espanso has unit tests and better support
* Espanso is multiplatform so also Windows and OSX

# How contribute

With [manageterms-gui.py](https://github.com/Mte90/espanso-typofixer/blob/master/tools/manageterms-gui.py) you can have a nice UI to add a single term manually to a word file. Next you can do a PR with your json with all the new words to this repository. This script requires `PyQT` installed.

Otherwise if you have a CSV file with [csvtoterms.py](https://github.com/Mte90/espanso-typofixer/blob/master/tools/csvtoterms.py) you can add automatically to the JSON file.

The [tools](https://github.com/Mte90/espanso-typofixer/tree/master/tools) folder includes also a script to remove duplicates.

## How generate a Espanso package

The words/typos list are in the words folder in JSON format, the [generator.py](https://github.com/Mte90/espanso-typofixer/blob/master/generator.py) script generate the `.yml` files for the various languages (for dependencies check the `requirements.txt` file).

## TODO

* Define how to upload the packages for espanso hub

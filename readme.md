# Espanso-Typofixer [![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)   

## Status (per last release)

* [![https://hub.espanso.org/typofixer-en](https://img.shields.io/badge/typofixer-%F0%9F%87%AC%F0%9F%87%A7%20%F0%9F%87%BA%F0%9F%87%B8-white.svg)]([https://hub.espanso.org/typofixer-en]): *<!--en-words-->17616<!--en-words-end-->* words with *<!--en-typos-->67204<!--en-typos-end-->* typos
* [![https://hub.espanso.org/typofixer-fr](https://img.shields.io/badge/typofixer-%F0%9F%87%AB%F0%9F%87%B7%20-white.svg)](https://hub.espanso.org/typofixer-fr): *<!--fr-words-->69<!--fr-words-end-->* words with *<!--fr-typos-->70<!--fr-typos-end-->* typos
* [![https://hub.espanso.org/typofixer-it](https://img.shields.io/badge/typofixer-%F0%9F%87%AE%F0%9F%87%B9%20-white.svg)](https://hub.espanso.org/typofixer-it): *<!--it-words-->1651<!--it-words-end-->* words with *<!--it-typos-->2145<!--it-typos-end-->* typos
* [![https://hub.espanso.org/typofixer-es](https://img.shields.io/badge/typofixer-%F0%9F%87%AA%F0%9F%87%B8%20-white.svg)](https://hub.espanso.org/typofixer-es): *<!--es-words-->103<!--es-words-end-->* words with *<!--es-typos-->118<!--es-typos-end-->* typos

## I want the development version!

Upload a new espanso package is very unconfortable right now, if it was possible I will release a new one every week automatically but every step is manual.
If you want the latest update word list, you need to follow that steps:

* Download this repository
* Execute the `generator.py` script
* Pick from the folders for every language the `package.yml` file
* Go on Linux to `/home/your-user/.config/espanso/match/packages/` and put that file in the corresponding package you installed
* Espanso (if running) will refresh automatically to the new terms

# How contribute

The word database is not inside the various `typofixer-*` folder by language but inside the [words](https://github.com/Mte90/espanso-typofixer/tree/master/words) folder in a JSON format.

With [manageterms-gui.py](https://github.com/Mte90/espanso-typofixer/blob/master/tools/manageterms-gui.py) you have a nice UI to add a single term manually to a word file. Next you can do a PR with your json with all the new words to this repository. This script requires `PyQT` installed.

Otherwise if you have a CSV file with [csvtoterms.py](https://github.com/Mte90/espanso-typofixer/blob/master/tools/csvtoterms.py) you can add automatically to the JSON file.

The [tools](https://github.com/Mte90/espanso-typofixer/tree/master/tools) folder includes also a script to remove duplicates.

## How generate a Espanso package

The [generator.py](https://github.com/Mte90/espanso-typofixer/blob/master/generator.py) script generate the `.yml` files for the various languages (for dependencies check the `requirements.txt` file).

# Story

Those packages were a porting [SyntaxAutoFix](https://github.com/Mte90/SyntaxAutoFix) in Python that is now 7 years old (in 2022).
Just used by me and no one else, in the years got tons of words with various hacktoberfest and by daily gathering of typos in English and Italian.

I preferred to migrate to [Espanso](https://espanso.org) for various reasons:

* I don't have to maintain a project by code, just still gather typos
* Python project require `sudo`
* Python project use like 50mb of ram, espanso instead less
* Opening to a wide more usage to gather more typos
* Espanso has unit tests and better support
* Espanso is multiplatform so also Windows and OSX
* Espanso support any uppercase/lowercase letters or mixed

## TODO

* Looking for an automated way to publish new packages on espanso hub

# Espanso-Typofixer

This packages is a porting [SyntaxAutoFix](https://github.com/Mte90/SyntaxAutoFix) in Python that is now 7 years old.  
Just used by me and no one else, in the years got tons of words with various hacktoberfest and by daily gathering of typos in English and Italian.

I preferred to migrate to Espanso for various reasons:

* I don't have to maintain a project by code, just still gather typos
* Python project require `sudo`
* Python project use like 50mb of ram, espanso instead more less
* Opening to a wide more usage to gather more typos

## How works

The words list are in the words folder in JSON format, the `generator.py` script generate the `.yml` files for the various languages.

The `tools` folder includes some script to convert a CSV to JSON and removed duplicates.

## TODO

* Update Readme with numbers for all the languages
* Define how to upload the packages for espanso hub
* Fix `tools` to work outside the original python project

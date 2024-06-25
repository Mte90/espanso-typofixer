#!/usr/bin/env python3
import argparse
import logging
import os.path
from SyntaxAutoFix.utils import open_typo_file, save_typo_data

logging.basicConfig(level=logging.INFO)


def parse_argument(_parser_):
    _parser_.add_argument('-lang', dest="lang", type=str, required=True)
    args = _parser_.parse_args()
    return args


def load_language(_args_, script_path):
    try:
        lang_path = script_path + _args_.lang + '.json'
        logging.info(
            f"Language {lang_path} loaded."
        )
        words = open_typo_file(lang_path)
        return words
    except FileNotFoundError:
        raise ValueError(f"Language '{ _args_.lang}' is not available.")


def main():
    # Parse argument
    parser = argparse.ArgumentParser(description='validate terms!')
    args = parse_argument(parser)

    # Store argument
    script_path = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_path, '../words/')
    words = load_language(args, script_path)
    cleaned_words = {}
    logging.info(
        f"Started processing"
    )
    for (correct, wrongs) in words.items():
        for wrong in wrongs:
            if wrong == correct:
                logging.info(
                    f"ERR 2: The term '{correct}' is a typo of itself."
                )
                del words[correct][words[correct].index(correct)]
                continue
            if not wrong:
                logging.info(f"ERR 1: The term '{correct}' has an empty typo.")
        _words = [*set(wrongs)]
        cleaned_words[correct] = _words

    logging.info(
        f"NOTICE: File cleaned by typos duplicated."
    )
    save_typo_data(script_path + args.lang + '.json', cleaned_words)


if __name__ == "__main__":
    main()

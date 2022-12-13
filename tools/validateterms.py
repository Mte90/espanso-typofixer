#!/usr/bin/env python3
import argparse
import logging
import os.path
from SyntaxAutoFix.utils import open_typo_file, save_typo_data


def parse_argument(_parser_):
    _parser_.add_argument('-lang', dest="lang", type=str, required=True)
    args = _parser_.parse_args()
    return args


def load_language(_args_, script_path):
    try:
        lang_path = script_path + _args_.lang + '.json'
        words = open_typo_file(lang_path)
        return words
    except FileNotFoundError:
        raise ValueError(f"Language '{ _args_.lang}' is not available.")


def term_is_typo_of_another_word(term, words):
    for (correct, wrongs) in words.items():
        if correct == term:
            logging.info(f"ERR 1: The term '{correct}' is a typo of '{term}'.")
        for wrong in wrongs:
            if not wrong:
                logging.info(f"ERR 3: The term '{correct}' has an empty typo.")


def main():
    # Parse argument
    parser = argparse.ArgumentParser(description='validate terms!')
    args = parse_argument(parser)

    # Store argument
    script_path = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(script_path, '../words/')
    words = load_language(args, script_path)
    cleaned_words = {}
    for (correct, wrongs) in words.items():
        for wrong in wrongs:
            if wrong == correct:
                logging.info(
                    f"ERR 2: The term '{correct}' is a typo of itself."
                )
                continue
            if wrong:
                term_is_typo_of_another_word(wrong, words)
        _words = [*set(wrongs)]
        cleaned_words[correct] = _words

    logging.info(
        f"NOTICE: File cleaned by typos duplicated."
    )
    save_typo_data(script_path + args.lang + '.json', cleaned_words)


if __name__ == "__main__":
    main()

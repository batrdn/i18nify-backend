from enchant import Dict
import re

def check_word(word):
    if word is None or word.strip() == '':
        return False
    # Checks for cyrillic text
    if bool(re.search('[а-яА-Я]', word)):
        return True
    # Checks for English text
    eng_dict = Dict("en_US")
    if eng_dict.check(word):
        return True
    # Checks for German text
    german_dict = Dict("de_DE")
    if german_dict.check(word):
        return True

    return False

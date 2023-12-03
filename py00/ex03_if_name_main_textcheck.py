import string
import sys

text = sys.argv[1:]
if len(text) > 1:
    print('Too many arguments, only one string is expected')
    exit()

def text_analyser(text):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    try:
        text = str(text)
    except:
        print('Function text_analyser() expects a string as argument')
        return
    majuscule = 0
    minuscule = 0
    ponctuation = 0
    espace = 0
    for i in text:
        if i.isupper():
            majuscule += 1
        elif i.islower():
            minuscule += 1
        elif i.isspace():
            espace += 1
        elif i in string.punctuation:
            ponctuation += 1
    print('The text contains', len(text), 'characters:\n', majuscule, 'upper letters\n', minuscule, 'lower letters\n', ponctuation, 'punctuation signs\n', espace, 'spaces')
    return
if __name__ == '__main__':
    text_analyser(text[0])
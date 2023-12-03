import string
import random

def generator(text, sep=" ", option=None):
    '''Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
    option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    '''
    printable_chars = set(string.printable)
    if isinstance(text, str):       
        if all(char in printable_chars for char in text):
            splited_text = text.split(sep)
            if option == "shuffle":
                while len(splited_text) > 0:
                    i = random.randint(0, len(splited_text) - 1)
                    yield splited_text.pop(i)
            elif option == "unique":
                i = 0
                while i < len(splited_text):
                    if splited_text[i] in splited_text[:i]:
                        splited_text.pop(i)
                    else:
                        i += 1
                for sub_string in splited_text:
                        yield sub_string
            elif option == "ordered":
                sort_splited_text = sorted(splited_text)
                for sub_string in sort_splited_text:
                    yield sub_string
            elif option == None:
                for sub_string in splited_text:
                    yield sub_string
            else:
                raise ValueError("\033[91mLa opción no es válida")
        else:
            raise ValueError("\033[91mEl texto contiene caracteres no imprimibles")
    else:
        raise ValueError("\033[91mEl texto no es una cadena de caracteres")

#text = "Le Lorem Ipsum est simplement du faux texte."
#text = 1.0
#for word in generator(text, sep=" "):
    #print(word)
#for word in generator(text, sep=" ", option="unique"):
    #print(word)
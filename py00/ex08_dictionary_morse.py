import sys

dictionary_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',  'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',  'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',  '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

arg = sys.argv[1:]
if len(arg) == 0:
    print("No arguments given.")

arg = ' '.join(arg)
for i in arg:
    if not i.isalpha() | i.isspace() | i.isdigit():
        print("ERROR")
        exit()
for j in arg:
    print(dictionary_morse[j.upper()], end=' ')
print()


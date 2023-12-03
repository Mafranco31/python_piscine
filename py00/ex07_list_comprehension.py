import sys
import string

arg = sys.argv[1:]

num = 0

def ft_check_arg(arg):
    if len(arg) != 2:
        print("ERROR")
        return False
    try:
        num = int(arg[1])
    except:
        print("ERROR")
        return False
    return True

if not ft_check_arg(arg):
    exit()
num = int(arg[1])
i = 0
word = ""
lettres = [i for i in arg[0] if i not in string.punctuation]
i = 0
mots_longs = []
for i in lettres:
    if i == " ":
        if len(word) >= num:
            mots_longs.append(word)
        word = ""
    else:
        word += i
if len(word) >= num:
    mots_longs.append(word)
print(mots_longs)
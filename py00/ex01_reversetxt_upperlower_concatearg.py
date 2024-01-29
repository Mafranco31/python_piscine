import sys

# Accessing command-line arguments
script_name = sys.argv[0]
arguments = sys.argv[1:]
arguments = ' '.join(arguments)

if  len(sys.argv) == 1:
    print('You must enter a string as argment.')

def reverse_text(input_text):
    result = ''
    for char in input_text:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) - ord('A') + ord('a'))
        else:
            result += char
    return result[::-1]

rev_arg = reverse_text(arguments)
print(rev_arg)

import sys

arg = sys.argv[1:]

if not arg:
    print('You must enter an integer as argment.')

elif len(arg) == 1:
    try:
        arg = int(arg[0])
    except ValueError:
        print('You must enter an integer as argment.')
        sys.exit()
    if arg == 0:
        print('I\'m Zero.')
    elif arg % 2 != 0:
        print('I\'m Odd.')
    else:
        print('I\'m Even.')
else:
    print('You must enter only one integer as argment.')
    
def what_are_the_vars(*args, **kwargs):
    """
        what_are_the_vars takes an unlimited number of arguments and returns
        a ObjectC object with the attributes set as the arguments.
        If an attribute already exists, the function returns None.
    """
    i = 0
    obj = ObjectC()
    for arg in args:
        var_name = "var_" + str(i)
        setattr(obj, var_name, arg)
        i += 1
    for key, value in kwargs.items():
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
    return obj

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
        obj = what_are_the_vars(7)
        doom_printer(obj)
        obj = what_are_the_vars(None, [])
        doom_printer(obj)
        obj = what_are_the_vars("ft_lol", "Hi")
        doom_printer(obj)
        obj = what_are_the_vars()
        doom_printer(obj)
        obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
        doom_printer(obj)
        obj = what_are_the_vars(42, a=10, var_0="world")
        doom_printer(obj)
        obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
        doom_printer(obj)
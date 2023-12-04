def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            A value, of same type of elements in the iterable parameter.
            None if the iterable can not be used by the function.
    """
    try:
        i = 0
        while i  + 1 < len(iterable):
            iterable[i] = function_to_apply(iterable[i], iterable[i + 1])
            iterable.pop(i + 1)
        return (iterable[0])
    except:
        return (None)

# lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# lst = [1, 2, 3]
# print(ft_reduce(lambda u, v: u + v, lst))
if __name__ == '__main__':
    from util import get_value
    x = {'a': 1, 'b': 52, 'd': 6}
    y = ['a', 'c', 'd']
    print(get_value(x, 'q'))
# Out[1]:  None

    print(get_value(x, 'a'))
# Out[2]:  1

    print(get_value(x, 'b'))
# Out[3]:  52

    print(get_value(y, 'b'))
# Out[4]:  None

    print(get_value(y, 'd'))
# Out[5]:  2

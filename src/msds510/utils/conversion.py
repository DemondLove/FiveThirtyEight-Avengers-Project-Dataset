'''
Module with functions used to covert floats to integers and ff the items are a list or tuple, the function should return the integer index of where
    the value is in the sequence. Or if the items are a dictionary, it should return the value associated with the input key.
'''
def to_int(x):
    """
    Converts an input value into an integer

    :param x: float
    :return: int
    """
    try:
        return int(x)
    except:
        return None


def get_value(items, value):
    """
    If the items are a list or tuple, the function should return the integer index of where
    the value is in the sequence.

    If the items are a dictionary, it should return the value associated with the input key.

    :param items: tuple, list, or dict
    :param value: index if tuple or list; value if dict
    :return:
    """
    try:
        return items[value]
    except KeyError:
        return None
    except TypeError:
        try:
            return items.index(value)
        except ValueError:
            return None
    except ValueError:
        return None

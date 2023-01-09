#!/usr/bin/python3
'''
Function that returns True ited (directly or indirectly) from the specified cif the object is an instance of a class that
inherlass; otherwise False
'''


def inherits_from(obj, a_class):
    '''
    Arguments:
    @obj: object to evaluate
    @a_class: class instance
    Return:
    True if the object is an instance of a class that inherited,
    otherwise False
    '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False

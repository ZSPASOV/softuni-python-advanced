# Here we illustrate how user-defined exceptions can be used in a program to raise errors
# define Python user-defined exceptions

class Error(Exception):
    '''Base class for other exceptions'''
    pass

class ValueTooSmallError(Error):
    '''Raised when the input value is too small'''

num = int(input())
if num < 10:
    raise ValueTooSmallError
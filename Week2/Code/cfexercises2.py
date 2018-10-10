#!/usr/bin/env python3

"""Some more functions exemplifying the use of control statements.
Practical 1, Week2"""

__author__ = 'Samraat Pawar (s.pawar@imperial.ac.uk)'
__version__ = '0.0.1'

#import
import sys


def foo1(x):
    """Square root
    """
    return x ** 0.5

def foo2(x, y):
    """Return larger number"""
    if x > y:
        return x
    return y #else


def foo3(x, y, z):
    """Reorder numbers"""
    if x > y:
        tmp = y
        y = x
        x = tmp
    if y > z:
        tmp = z
        z = y
        y = tmp
    return [x, y, z]


def foo4(x):
    """ Exclamation mark"""
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo5(x): # a recursive function
    """Example of a recursive function"""
    if x == 1:
        return 1
    return x * foo5(x - 1)


def main(argv):
    """ Returns example results based on test arguments""" 
    print(foo1(22))
    print(foo2(33,2))
    print(foo3(120,72,1))
    print(foo4(121))
    print(foo5(6))
    return 0


print(1)
if __name__ == "__main__": # This main has nothing to do with the name of any of my functions
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv) # This main links to the name of my last function
    sys.exit(status)
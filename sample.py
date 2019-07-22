import os
import random
import this

from django.utils.safestring import mark_safe


x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

    
def some_function():
    print("this should raise a documentation related issue.")
    raise NotImplemented


def some_other_function():
    print("this should raise a documentation related issue.")
    # SKIPCQ
    # Some other comment
    # Yet another comment
    raise NotImplemented

    
def dummy_function():
    print('foo')

def new_dummy_function():
    print('foobar')
    map()
    try:
        input = 10
    except Exception as input:
        pass
    raise NotImplemented  # skipcq: PYL-E0702

def o_yeah_function():
    mark_safe("<b>sfjbgfadfgbsf</b>")

class Klass:
    def __init__(self):
        pass

    # This function does not use `self`.
    # Hence an issue will be raised. Lets ignore it.
    def func(self, x):  # skipcq
        return x ** 2

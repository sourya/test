import os
import random
import this

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

    
def some_function():
    print("this should raise a documentation related issue.")


def some_other_function():
    print("this should raise a documentation related issue.")
    raise NotImplemented

    
def dummy_function():
    print('foo')

def new_dummy_function():
    print('foobar')
    raise NotImplemented

def o_yeah_function():
    raise NotImplemented

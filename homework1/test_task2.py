from task2 import *

# test if each method actually returns an instance of said datatype
def test_int():
    assert isinstance(someint(), int), "Expected an integer"

def test_float():
    assert isinstance(somefloat(), float), "Expected a float"

def test_str():
    assert isinstance(somestr(), str), "Expected a string"

def test_bool():
    assert isinstance(somebool(), bool), "Expected a boolean"
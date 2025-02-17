from task4 import *

def test_discount_int_int():
    assert calculate_discount(50, 50) == 25

def test_discount_int_float():
    assert calculate_discount(100, 5.5) == 94.5

def test_discount_float_float():
    assert calculate_discount(80.7, 10.5) == 72.2265

def test_discount_float_int():
    assert calculate_discount(33.5, 30) == 23.45
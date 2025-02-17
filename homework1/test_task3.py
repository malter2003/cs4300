from task3 import *

def test_sign_pos():
    assert get_sign(10) == 1

def test_sign_zero():
    assert get_sign(0) == 2

def test_sign_neg():
    assert get_sign(-29) == 3

def test_for_loop():
    assert for_loop() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_while_loop():
    assert while_loop() == 5050
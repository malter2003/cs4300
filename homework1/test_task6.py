import os
from task6 import *

def test_word_count(filename, expected_count):
    actual_count = count_words(filename)
    assert actual_count == expected_count, f"Expected {expected_count}, got {actual_count}"

def pytest_generate_tests(metafunc):
    if "filename" in metafunc.fixturenames:
        filename = 'task6_read_me.txt'
        expected_word_count = 126
        metafunc.parametrize(
            "filename, expected_count", 
            [(filename, expected_word_count)],
            ids=[f"test_{os.path.splitext(filename)[0]}"]
        )
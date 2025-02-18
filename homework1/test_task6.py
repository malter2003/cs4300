import os
from task6 import *

# actual function logic
def test_word_count(filename, expected_count):
    actual_count = count_words(filename)
    assert actual_count == expected_count, f"Expected {expected_count}, got {actual_count}"

# hook on to this to generate a function
def pytest_generate_tests(metafunc):
    if "filename" in metafunc.fixturenames: # ensure the test function requires a filename param
        filename = 'task6_read_me.txt' # define filename to read and expected word count
        expected_word_count = 126
        
        # parameterize test function
        metafunc.parametrize(
            "filename, expected_count", 
            [(filename, expected_word_count)], # provide test data 
            ids=[f"test_{os.path.splitext(filename)[0]}"] # generate the id of the test based on the filename
        )
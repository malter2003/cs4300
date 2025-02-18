from task5 import *

def test_books():
    assert books()[:3] == [ # slice list to retrieve first 3 from the list
        ("Hunter X Hunter", "Yoshihiro Togashi"), 
        ("Monster", "Naoki Urasawa"), 
        ("Vinland Saga", "Makoto Yukimura")
    ]

def test_students():
    result = students()
    assert result["John Smith"] == 394 # access keys to get values
    assert result["Sarah Ginsburth"] == 925
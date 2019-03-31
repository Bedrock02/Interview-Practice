from replace_spaces import *


def test_replace_spaces():
    assert replace_space("Test This  ") == "Test%20This%20%20"
    assert replace_space_2("Test This  ") == "Test%20This%20%20"
    assert replace_space_3("Test This  ") == "Test%20This%20%20"

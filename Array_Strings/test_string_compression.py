from string_compression import *


def test_compression():
    assert compress_string('aabcccccaaa') == 'a2b1c5a3'
    # assert compress_string2('aabcccccaaa') == 'a2b1c5a3'

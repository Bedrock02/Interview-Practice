from linked_list_hash import *

def test_add_to_hash():
    my_hash = linked_hash()
    my_hash['cat'] = 'meow'
    assert len(my_hash) == 1

    my_hash['cat'] = 'meowwww'
    assert len(my_hash) == 1

    my_hash['dog'] = 'wof'
    assert len(my_hash) == 2

def test_delete_hash_item():
    my_hash = linked_hash()
    my_hash['cat'] = 'meow'
    assert len(my_hash) == 1

    del my_hash['cat']
    assert len(my_hash) == 0

def test_str():
    my_hash = linked_hash()
    my_hash['cat'] = 'meow'
    assert str(my_hash) == "{ cat:meow, }"

    my_hash['cat'] = 'meowwww'
    assert str(my_hash) == "{ cat:meowwww, }"

    my_hash['dog'] = 'wooooff'
    assert str(my_hash) == "{ cat:meowwww, dog:wooooff, }"

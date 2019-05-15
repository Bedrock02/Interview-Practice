from trie import *

def test_trie_search():
    my_trie = Trie()
    my_trie.insert("cat")
    assert my_trie.search("cat") == True
    assert my_trie.search("ca") == False
    assert my_trie.search("blah") == False

def test_trie_print_out_words():
    my_trie = Trie()
    my_trie.insert("cat")
    my_trie.insert("cattle")
    my_trie.insert("dog")
    assert sorted(my_trie.print_out_words()) == sorted(["cat", "dog", "cattle"])

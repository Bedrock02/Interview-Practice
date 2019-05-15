from trie import *

def test_trie_search():
    my_trie = Trie()
    my_trie.insert("cat")
    assert my_trie.search("cat") == True
    assert my_trie.search("ca") == False
    assert my_trie.search("blah") == False

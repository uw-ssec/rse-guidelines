from reverse import reverse_each_word, reverse_in_place


def test_reverse():
    x = list("hello")
    reverse_in_place(x)
    assert "".join(x) == "olleh"


def test_reverse_words():
    x = list("hello world")
    reverse_each_word(x)
    assert "".join(x) == "olleh dlrow"

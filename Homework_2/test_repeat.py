import repeat


def test_repeat():
    assert hasattr(
        repeat, 'repeat'), "Your repeat.py script must have a method called repeat"

    assert repeat.repeat('a', 1) == 'a'
    assert repeat.repeat('now', 2) == 'nnooww'
    assert repeat.repeat(
        'Python is fun', 5) == 'PPPPPyyyyyttttthhhhhooooonnnnn     iiiiisssss     fffffuuuuunnnnn'
    assert repeat.repeat(
        'osnabrueck', 4) == 'oooossssnnnnaaaabbbbrrrruuuueeeecccckkkk'

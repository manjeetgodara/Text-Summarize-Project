
def test_1():
    x=1
    y=1
    assert x==y

def test_2():
    str = "selenium"
    sentence = "selenium is important"
    assert str in sentence

def test_3():
    str = "jenkins"
    sentence = "jenkins is present"
    assert str in sentence , "str does not exists"
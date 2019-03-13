#encoding:utf-8
import pytest

def test_hello():
    print("hello world")
    assert 1

@pytest.mark.xfail()
def test_yoyo1():
    a="hello"
    b="hello world"
    assert a==b

@pytest.mark.xfail()
def test_yoyo2():
    a="hello"
    b="hello,world"
    assert a != b

if __name__=='__main__':
    pytest.main(["-v",""])
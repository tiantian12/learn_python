#encoding=utf-8
import pytest

@pytest.fixture()
def user():
    print("获取用户名")
    a="yoyo"
    assert a=="yoyo123"
    return a

def test_1(user):
    assert user=="yoyo"

if __name__=="__main__":
    pytest.main(["-s","test_fixture3.py"])
#encoding=utf-8

import pytest

@pytest.fixture(scope="module")
def first():
    print("\n获取用户名，scope为module级别当前.py模块只运行一次")
    a="yoyo"
    return a

def test_1(first):
    print("测试账号：%s" % first)
    assert first=="yoyo"

class TestCase():
    def test_2(self,first):
        print("测试账号：%s" % first)
        assert first=="yoyo"

if __name__=="__main__":
    pytest.main(["-s","test_fixture10.py"])
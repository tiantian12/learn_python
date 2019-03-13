#encoding:utf-8

import pytest

@pytest.fixture()
def first():
    print("\n获取用户名")
    a="yoyo"
    return a

@pytest.fixture(scope="function")
def second():
    print("\n获取密码")
    b="123456"
    return b

class TestCase():
    def test_1(self,first):
        print("测试账号： %s" % first)
        assert first=="yoyo"

    def test_2(self,second):
        print("测试密码：%s" % second)
        assert second=="123456"

if __name__=="__main__":
    pytest.main(["-s","test_fixture8.py"])
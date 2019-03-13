#coding=utf-8

import pytest

@pytest.fixture(scope="class",autouse=True)
def first():
    print("获取用户名，scope为class只运行一次")
    a="yoyo"
    return a

class TestCase():
    def test_1(self,first):
        print("测试账号:%s" % first)
        assert first=="yoyo"

    def test_2(self,first):
        print("测试账号：%s" % first)
        assert first=="yoyo"

if __name__=='__main__':
    pytest.main(["-s","test_fixture9.py"])
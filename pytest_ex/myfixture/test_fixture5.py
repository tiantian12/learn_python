#encoding:utf-8

import pytest

@pytest.fixture()
def user():
    print("获取用户名")
    a="yoyo"
    return a

@pytest.fixture()
def psw():
    print("获取密码")
    b="123456"
    return b

def test_1(user,psw):
    print("测试账号：%s,密码：%s" %(user,psw))
    assert user=="yoyo"

if __name__=='__main__':
    pytest.main(["-s","test_fixture5.py"])
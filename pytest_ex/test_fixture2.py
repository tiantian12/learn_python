#encoding:utf-8
import pytest

def test_s4(login):
    print("用例4：登录之后其他动作111")

def test_s5():
    print("用例5：不需要登录，动作222")

if __name__=='__main__':
    pytest.main(["-s","test_fixture2.py"])
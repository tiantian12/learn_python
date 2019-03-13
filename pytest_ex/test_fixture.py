#coding:utf-8

import pytest

def test_s1(login):
    print("用例1：登录之后其他动作111")

def test_s2():
    print("用例2：不需要登录，其他动作222")

def test_s3(login):
    print("用例3：登录之后其他动作333")

if __name__=='__main__':
    pytest.main(['-s','test_fixture.py'])
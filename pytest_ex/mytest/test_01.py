#coding:utf-8
import pytest

test_login_data=[("admin","11111"),("test","")]

def login(user,psw):
    print("登录账号：%s" %user)
    print("密码：%s" %psw)
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("user,psw",test_login_data)
def test_login(user,psw):
    result=login(user,psw)
    assert result==True,"失败原因，密码为空"

if __name__=='__main__':
    pytest.main(["-s","test_01.py"])
#coding:utf-8
import pytest

test_user_data=[{"user":"admin","psw":"11111"},{"user":"admin1","psw":""}]

@pytest.fixture(scope="module")
def login(request):
    user=request.param["user"]
    psw=request.param["psw"]
    print("登录账户：%s" % user)
    print("密码：%s" %psw)
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_login(login):
    a=login
    print("测试用例中login的返回值 %s" %a)
    assert a,"失败原因，密码为空"


if __name__=='__main__':
    pytest.main(["-s","test_03.py"])
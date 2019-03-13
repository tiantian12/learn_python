#coding:utf-8
import pytest

test_user_data=["admin1","admin2"]

@pytest.fixture(scope="module")
def login(request):
    print(request)
    user=request.param
    print("登录账户：%s" %user)
    return user

@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_login(login):
    a=login
    print("测试用例中login的值：%s" %a)
    assert a!=""

if __name__=='__main__':
    pytest.main(['-s',"test_02.py"])
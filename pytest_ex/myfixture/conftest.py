import pytest

@pytest.fixture(scope="session")
def first():
    print("\n获取用户名，scope为session级别可在多个.py模块只运行一次   test")
    a="yoyo"
    return a

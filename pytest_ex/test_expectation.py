#coding=utf-8
#参数化

import pytest

@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+4",6),pytest.param("6*9",42,marks=pytest.mark.xfail)])
def test_eval(test_input,expected):
    assert eval(test_input)==expected

if __name__=='__main__':
    pytest.main(["-s","test_expectation.py"])

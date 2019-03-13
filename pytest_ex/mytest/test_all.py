#encoding:utf-8
import pytest
from testcases import mytest
import os
import sys

if __name__=='__main__':
    os.system("pytest -s test_06.py test_07.py")
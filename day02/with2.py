#coding=utf-8
from contextlib import contextmanager
@contextmanager
def show():
    print("123")
    yield
    print("456")

with show():
    print("9999")

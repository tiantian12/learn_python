#encoding=utf-8
"""
 function:两个数相乘
 >>> multiply(4,3)
 12
 >>> multiply('a',3)
 'aaa'
 """
def multiply(a,b):

    return a*b

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
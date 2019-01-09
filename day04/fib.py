#-*-coding:utf-8-*-

def fib_func(arg1,arg2,stop):
    if arg1==0:
        print(arg1,arg2,end=" ")
    arg3=arg1+arg2
    print(arg3,end=" ")
    if arg3<stop:
        fib_func(arg2,arg3,stop)
fib_func(0,1,30)
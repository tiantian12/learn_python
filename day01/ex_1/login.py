#coding=utf-8
import sys

#定义登录计数
login_count=0
#登录前先判断是否被锁定:lock_type为0，则正常，为1，则被锁定
f=open("lock.txt","r")
lock_type=int(f.read())
f.close()
#判断锁定类型
if lock_type==1:
    print("你已被锁定！！！")
    sys.exit()
else:
    while login_count<3:
        username=input("请输入用户名：")
        password=input("请输入密码：")
        if username=="admin" and password=="123456":
            print("欢迎登录")
            break
        print("请重新输入....")
        login_count+=1
    else:
        print("你已被锁定！！！")
        f=open("lock.txt","w")
        f.write("1")
        f.close()
        sys.exit()
print("do something !!!")



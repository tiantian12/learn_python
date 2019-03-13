#-*- coding:utf-8 -*-
import sys
from ShopMall.UserManage.User import User

print("""
    欢迎进入系统
    1.登录
    2.注册
    3.修改密码
    4.退出系统
    """)
while True:
    choice=input("请输入的选项 1/2/3/4:")
    try:
        #登录
        if int(choice)==1:
            name=input("请输入账号：")
            pwd=input("请输入密码：")
            #执行登录
            user=User()
            login_flag, locked, msg=user.login(name,pwd)
            if login_flag==True:
                print("登录成功："+msg)
            elif locked==True:
                print("账号已被锁定："+msg)
            else:
                print("登录失败："+msg)
                continue
        #注册
        elif int(choice)==2:
            name = input("注册账号：")
            pwd = input("密码：")
            #执行注册
            user=User()
            reg_status, msg=user.register(name,pwd)
            if reg_status:
                print("注册成功："+msg)
            else:
                print("注册失败："+msg)
        #修改密码
        elif int(choice)==3:
            name = input("请输入账号：")
            old_pwd = input("请输入旧密码：")
            new_pwd=input("请输入新密码：")
            #执行改密
            user=User()
            update_flag, msg=user.update_pwd(name,old_pwd,new_pwd)
            if update_flag:
                print("修改密码成功："+msg)
            else:
                print("修改密码失败："+msg)
        #退出系统
        elif int(choice)==4:
            sys.exit(0)
        else:
            print("输入有误，请重新输入")
    except ValueError:
        print("输入有误，请重新输入")

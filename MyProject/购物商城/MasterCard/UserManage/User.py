#-*- coding:utf-8 -*-
"""
提供如下功能：
    1.登录
    2.注册
    3.修改密码

users.txt文件格式：
   {accout:{"pwd":密码,"login_num":登录次数}}

"""


import json

class User(object):
    def __init__(self):
        with open("users.txt","r+") as f:
            if not f.read():
                json.dump({},f)

    def login(self,name,pwd):
        #登录成功和账户状态标志位
        login_flag=False
        locked=False
        msg=""

        with open("users.txt","r+") as f:
            users = json.load(f)
            if not users:
                msg="暂无账号数据，请先注册"
                return login_flag,locked,msg
            try:
                if name in users and users[name]["login_num"]<=3:
                    if users[name]["pwd"]==pwd:
                        users[name]["login_num"]=0
                        login_flag=True
                        msg="登录成功"
                    else:
                        users[name]["login_num"] +=1
                        msg="账号或密码错误，如无账号，请先注册"
                else:
                    locked=True
                    msg="你的账号已被锁定"
            except KeyError:
                msg="账号或密码错误，如无账号，请先注册"

            #更新登录次数数据
            f.seek(0)
            f.truncate()
            json.dump(users,f)

            return login_flag,locked,msg

    def register(self,name,pwd):
        #注册状态
        reg_status=False
        msg=""

        with open("users.txt","r+") as f:
            users=json.load(f)
            if name in users:
                msg="账号已存在,请登录"
            else:
                f.seek(0)
                f.truncate()
                users[name]={"pwd":pwd,"login_num":0}
                json.dump(users,f)
                reg_status=True
                msg="账号注册成功，请登录"
        return reg_status,msg

    def update_pwd(self,name,old_pwd,new_pwd):
        #更新状态
        update_flag=False
        msg=""

        with open("users.txt","r+") as f:
            users=json.load(f)
            if not users:
                msg="暂无账号数据，请先注册"
                return update_flag,msg
            try:
                if name in users and users[name]["login_num"]<=3:
                    if users[name]["pwd"]==old_pwd:
                        users[name]["pwd"]=new_pwd
                        update_flag=True
                        msg="修改密码成功"
                    else:
                        users[name]["login_num"]+=1
                        msg="账号或密码错误，修改失败"
                else:
                    msg="你的账号已被锁定"
            except KeyError:
                msg="账号或密码错误，如无账号，请先注册"
            # 更新登录次数数据
            f.seek(0)
            f.truncate()
            json.dump(users, f)

            return update_flag,msg


if __name__=='__main__':
    user=User()
    a=user.register("1222","ffsd1")
    print(a)

#coding=utf-8
import sys

while True:
    print("""
                1.广东省
                2.湖南省
                3.江西省
                4.湖北省
                """)
    province=input("请选择省份(返回上一级输入b)：")
    while True:
        if province=="1":
            print("""
                1.深圳市
                2.惠州市
                3.东莞市
                """)
            city=input("请选择城市(返回上一级输入b)：")
            if city=="1":
                while True:
                    print("""
                    1.罗湖区
                    2.南山区
                    3.福田区
                    4.宝安区
                    """)
                    zone=input("请选择区(返回上一级输入b)：")
                    if zone=="1":
                        print("罗湖区")
                    elif zone=="2":
                        print("南山区")
                    elif zone=="3":
                        print("福田区")
                    elif zone==4:
                        print("宝安区")
                    elif zone=="b":
                        break
                    else:
                        print("error")
            elif city=="2":
                pass
            elif city=="3":
                pass
            elif city=="4":
                pass
            elif city=="b":
                break
            else:
                print("error")
        elif province=="2":
            pass
        elif province=="3":
            pass
        elif province=="4":
            pass
        elif province=="b":
            sys.exit()
        else:
            print("error")

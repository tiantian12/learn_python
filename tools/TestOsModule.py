#coding:utf-8

import os
#文件名
print(__file__)
#文件绝对路径
print(os.path.abspath(__file__))
#文件所在目录
print(os.path.dirname(os.path.abspath(__file__)))

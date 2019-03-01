#coding=utf-8

import time
#时间
dt="2019-2-23 13:33:45"
#转换成时间数组
timeArray=time.strptime(dt,"%Y-%m-%d %H:%M:%S")
print(timeArray)
#转换成时间戳
timestamp=time.mktime(timeArray)
print(timestamp)

#时间
dt="2019-2-23 13:33:45"
#转换成时间数组
timeArray=time.strptime(dt,"%Y-%m-%d %H:%M:%S")
#转换成新的时间格式
dt_new=time.strftime("%Y%m%d-%H:%M:%S",timeArray)
print(dt_new)

#时间戳
timestamp=2111111111
#转换成localtime
time_local=time.localtime(timestamp)
#转换成时间格式：%Y_%m_%d %H:%M:%S
dt=time.strftime("%Y_%m_%d %H:%M:%S",time_local)
print(dt)

#获取当前时间
time_now=time.time()
#转换成localtime
time_local=time.localtime(time_now)
#转换成时间格式：%Y--%m--%d %H:%M:%S
dt=time.strftime("%Y--%m--%d %H:%M:%S",time_local)

print(dt)
import requests
import json

#不带参get请求
#r=requests.get("http://httpbin.org/get")

#带参get请求
# myParams={"username":"test","password":"12345"}
# r=requests.get("http://httpbin.org/get",params=myParams)

#不带参post请求
#r=requests.post("http://httpbin.org/post")

#带参post请求
# myData={"username":"test","password":"123456"}
# r=requests.post("http://httpbin.org/post",data=myData)

#提交json数据的post请求
# myData={"username":"test","password":"123456"}
# r=requests.post("http://httpbin.org/post",data=json.dumps(myData))

#通过post请求提交图片
# myfile={"file1":open("C:\\Users\\clareliu\\Desktop\\1.png","rb")}
# r=requests.post("http://httpbin.org/post",files=myfile)

#建立会话后,通过会话发送get/post请求
#s=requests.Session()
#get请求
#r=s.get("http://httpbin.org/get")
#post请求
#r=s.post("http://httpbin.org/post")


# print(r.text)
# print(r.content)
# print(r.url)
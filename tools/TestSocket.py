from  socket import *

#主机地址
myhost=""
#端口
myport=9000

#创建Socket对象
socketObj=socket(AF_INET,SOCK_STREAM)

#绑定端口
socketObj.bind((myhost,myport))

#允许64个连接
socketObj.listen(64)

#一直运行
while True:
    connection,address=socketObj.accept()

    print("connect:",address)

    while True:
        #接收数据
        data=connection.recv(1024)
        print(data)
        if not data:
            break
        #处理数据，返回给发送端
        connection.send(data.upper()+b"\n")
    #关闭连接
    connection.close()

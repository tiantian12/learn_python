from socketserver import TCPServer,BaseRequestHandler

class MyRequestHandler(BaseRequestHandler):

    def handle(self):
        print("connection:",self.client_address)

        while True:
            data=self.request.recv(1024)
            if not data:
                break
            self.request.send(data.upper()+b"\n")

if __name__=='__main__':
    myHost=""
    myPort=9191
    serverObj=TCPServer((myHost,myPort),MyRequestHandler)
    serverObj.serve_forever()
from socketserver import ThreadingTCPServer,StreamRequestHandler

class MyStreamRequestHandler(StreamRequestHandler):
    def handle(self):
        print("connection:",self.client_address)
        while True:
            data=self.request.recv(1024)
            if not data:
                break
            self.request.send(data.upper()+b"\n")
        self.request.close()

if __name__=='__main__':
    myHost=""
    myPort=9292
    serverObj=ThreadingTCPServer((myHost,myPort),MyStreamRequestHandler)
    serverObj.serve_forever()
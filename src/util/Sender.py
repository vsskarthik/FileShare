import requests


class Sender:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.conn = False
        self.url = None
        try:
            requests.post(f"http://{self.ip}:{self.port}")
            self.conn = True
            self.url = f"http://{self.ip}:{self.port}"
        except:
            print(f"[INFO] Connection to {self.ip} on port {self.port} failed")

    
    def send_file(self,file_obj):
        if(file_obj == None):
            return
        try:
            files = {'file': open('test.txt', 'rb')}
            requests.post(self.url, files=files)
        except:
            print(f"[INFO] Connection to {self.ip} on port {self.port} failed")
    
    def read_file(self,filepath):
        try:
            return open(filepath,'rb')
        except:
            print("File Not Found. Please Select a valid file")
            return None
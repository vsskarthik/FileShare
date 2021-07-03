import requests


class Sender:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.conn = False
        self.url = None
        try:
            r = requests.head(f"http://{self.ip}:{self.port}")
            if(r.status_code == 200):
                print(f"[SUCCESS] Connected to {self.ip}")
                self.conn = True
                self.url = f"http://{self.ip}:{self.port}"
        except:
            print(f"[ERROR] Connection to {self.ip} on port {self.port} failed")

    
    def send_file(self,file_obj):
        if(file_obj == None):
            return [False,404]
        try:
            files = {'file': file_obj}
            r = requests.post(self.url, files=files)
            if(r.status_code == 200):
                print("[SUCCESS] File sent successfully")
                return [True,200]
            elif(r.status_code == 405):
                print("[FAILED] File declined by receiver")
                return [False,405]
            else:
                print("[ERROR] File was not sent. Please try again")
                return [False,500]
        except:
            print(f"[ERROR] Connection to {self.ip} on port {self.port} failed")
            return [False,404]
    def read_file(self,filepath):
        try:
            return open(filepath,'rb')
        except:
            print("[ERROR] File not sent. Please select a valid file")
            return None
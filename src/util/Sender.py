import requests


class Sender:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.conn = False
        self.url = None
        try:
            r = requests.head(f"http://{self.ip}:{self.port}")
            print(r.status_code)
            self.conn = True
            self.url = f"http://{self.ip}:{self.port}"
        except:
            print(f"[ERROR] Connection to {self.ip} on port {self.port} failed")

    
    def send_file(self,file_obj):
        if(file_obj == None):
            return
        try:
            files = {'file': file_obj}
            r = requests.post(self.url, files=files)
            if(r.status_code == 200):
                print("[SUCCESS] File sent successfully")
            elif(r.status_code == 405):
                print("[FAILED] File declined by receiver")
            else:
                print("[ERROR] File was not sent. Please try again")
        except:
            print(f"[ERROR] Connection to {self.ip} on port {self.port} failed")
    
    def read_file(self,filepath):
        try:
            return open(filepath,'rb')
        except:
            print("[ERROR] File not sent. Please select a valid file")
            return None
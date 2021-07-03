import requests
import platform    
import subprocess
import os
from tcping import Ping

class Scanner:
    def ping(self,host,port):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', host]
        p = Ping(host,port)
        #return subprocess.call(command,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT) == 0
        p.ping(1)


    def check(self, ip, port):
        url = f"http://{ip}:{port}"
        try:
            r = requests.head(url, timeout=2)
            if(r.status_code == 200):
                return True
            return False
        except:
            return False

    def scan(self, ip_add: str, port):
        ip_range = '.'.join(ip_add.split('.')[:-1])
        print(f"Testing on Port: {port}")
        for i in range(1, 255):
            ip = ip_range+"."+str(i)
            #c = self.check(ip, port)
            try:
                c = self.ping(ip,port)
            except Exception as e:
                print(e)
                break
            print(f"{ip} -> {'SUCCESS' if c else 'FAIL'}")

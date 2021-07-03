from os import stat
from flask import Flask,Response,request
import logging
from flask import cli
cli.show_server_banner = lambda *_: None
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
import easygui
import socket

class Receiver:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.app = Flask(__name__)
        self.debug = True
 

    def create_handler(self):

        @self.app.route('/',methods=['GET','POST','HEAD'])
        def handle_file_tx():
            if request.method == "GET":
                return Response(status=405)
            elif request.method == "HEAD":
                print("Connection OK")
                return Response(status=200)
                
            else:
                try:
                    conf = input(f"{request.remote_addr} wants to send a file. Do you accept?(y/n)")
                    if(conf !="y"):
                        return Response(status=405)
                    print("reached")
                    filename = request.files.get('file').filename
                    save_path = easygui.filesavebox(default=filename)
                    filepath = save_path
                    request.files.get('file').save(filepath)
                    print("[Success] File Saved with name: "+filepath)
                    return Response(status=200)
                except Exception as e:
                    print("[Error] Failed to save received file. Please Try Again")
                    if self.debug:
                        print(e)
                        print("Error in create_handler/handle_file_tx Receiver")
                    return Response(status=500)

    def start_server(self):
        try:
            #print(f"Starting Server. {}")
            local_ip = socket.gethostbyname(socket.gethostname())
            print(f"Preparing to receive. Please enter your IP : {local_ip} on the sender side")
            self.app.run(host = self.host,port=self.port,debug=False)
        
        except Exception as e:
            if self.debug:
                print(e)
                print("Error in start_server - Receiver")
            print(f"[ERROR] Failed to start server on {self.host}:{self.port}.")
            
from flask import Flask,Response,request
import easygui

class Receiver:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.app = Flask(__name__)
 

    def create_handler(self):
        @self.app.route('/',methods=['GET','POST'])
        def handle_file_tx():
            if request.method == "GET":
                return Response(status=405)
            else:
                try:
                    if(request.files.get('file')!=None):
                        filename = request.files.get('file').filename
                        save_path = easygui.filesavebox(default=filename)
                        filepath = save_path
                        request.files.get('file').save(filepath)
                        print("[Success] File Saved with name: "+filepath);
                        return Response(status=200)
                    else:
                        print("Connection OK")
                except Exception as e:
                    print("[Error] Failed to save received file. Please Try Again")
                    print(e)
                    return Response(status=500)

    def start_server(self):
        try:
            self.app.logger.disabled = True
            self.app.run(host = self.host,port=self.port,debug=False)
        
        except:
            print(f"[ERROR] Failed to start server on {self.host}:{self.port}.")
            
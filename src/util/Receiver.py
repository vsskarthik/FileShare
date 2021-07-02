from flask import Flask,Response,request

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
                    filename = request.files.get('file').filename
                    request.files.get('file').save("recv_"+filename)
                    print("File Saved with name: "+"recv_"+filename);
                    return Response(status=200)
                except:
                    print("Error while saving file. Please Try Again")
                    return Response(status=500)

    def start_server(self):
        self.app.run(host = self.host,port=self.port,debug=True)

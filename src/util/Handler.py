from . import Sender
from . import Receiver




class Handler:
    def handle_send(self,ip,port,filepath):
        sender = Sender.Sender(ip,port)
        if(sender.conn):
            file = sender.read_file(filepath)
            sender.send_file(file)

    def handle_recv(self,ip,port):
        recv = Receiver.Receiver(ip,port)
        recv.create_handler()
        recv.start_server()
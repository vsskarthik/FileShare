from . import Sender
from . import Receiver
import easygui

class Handler:
    def check_conn(self,ip):
        return Sender.Sender(ip,2805).conn

    def handle_send(self,ip,filepath,port=2805):
        sender = Sender.Sender(ip,port)
        if(sender.conn):
            file = sender.read_file(filepath)
            return sender.send_file(file)
        else:
            return [False,404]

    def handle_recv(self,ip,port):
        recv = Receiver.Receiver(ip,port)
        recv.create_handler()
        recv.start_server()
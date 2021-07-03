from . import Sender
from . import Receiver
import easygui

class Handler:
    def handle_send(self,ip,port,filename=None):
        sender = Sender.Sender(ip,port)
        if(sender.conn):
            filepath = easygui.fileopenbox()
            file = sender.read_file(filepath)
            sender.send_file(file)

    def handle_recv(self,ip,port):
        recv = Receiver.Receiver(ip,port)
        recv.create_handler()
        recv.start_server()
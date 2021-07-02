from util import Sender

sender = Sender.Sender("192.168.0.107",2805)
if(sender.conn):
    file = sender.read_file("test.txt")
    sender.send_file(file)
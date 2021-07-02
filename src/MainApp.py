from util import Handler
import easygui

class App:
    def print_menu(self):
        print("Please select the action: ")
        print("1.Send")
        print("2.Receive")

    def send(self):
        handler = Handler.Handler()
        filepath = easygui.fileopenbox()
        handler.handle_send("192.168.0.107",2805,filepath)
        
    def recv(self):
        handler = Handler.Handler()
        handler.handle_recv("0.0.0.0",2805)

    def run(self):
        self.print_menu()
        ch = int(input())
        if(ch == 1):
            self.send()
        else:
            self.recv()

if __name__ == "__main__":
    app = App()
    app.run()
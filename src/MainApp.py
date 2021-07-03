from util import Handler


class App:
    def print_menu(self):
        print("Please select the action: ")
        print("1.Send")
        print("2.Receive")

    def send(self):
        handler = Handler.Handler()
        ip = input("Enter the IP Address of the reciever: ")
        handler.handle_send(ip,2805)
        
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
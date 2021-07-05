from send_screens import *
from recv_screens import *
from tkinter import *
from tkinter.ttk import *
import sys
sys.path.append('../')
from util import Handler

class App:
    def __init__(self):
        self.send_to_ip = None 
        self.handler = Handler.Handler()
        self.initialize_screens()
        self.root = Tk()
        self.root.title("Easy Share")
        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.create_send_screens()
        self.root.geometry("350x200")
        self.root.resizable(False, False)
        self.choice_screen.render()
        #test_button = Button(self.root, text="test",command=lambda:self.choice_screen.hide())
        #test_button.place(relx=0.5,rely=0.9,anchor=CENTER)
        self.root.mainloop()
    
    def initialize_screens(self):
        self.choice_screen = ChoiceScreen()
        #Send
        self.ip_input = IpInputScreen()
        self.file_input = FileScreen()
        #Recv
        self.conf_screen = ConfirmationScreen()
        self.info_screen = InfoScreen() 


    def create_send_screens(self):
        self.choice_screen.create(self)
        #Send
        self.ip_input.create(self)
        self.file_input.create(self)
        #Recv
        self.conf_screen.create(self)
        self.info_screen.create(self)
    
    def change_view(self,curr,next):
        curr.hide()
        next.render()
    
    def close(self):
        sys.exit(0)


if __name__ == "__main__":
    app = App()
    
from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox


class ChoiceScreen():
    def create(self,app):
        self.send_button = Button(app.root, text="Send",command=lambda: app.change_view(app.choice_screen,app.ip_input))
        self.recv_button = Button(app.root, text="Receive")
    
    def render(self):
        self.send_button.place(relx=0.3,rely=0.5,anchor=CENTER)
        self.recv_button.place(relx=0.7,rely=0.5,anchor=CENTER)
    
    def hide(self):
        self.send_button.place_forget()
        self.recv_button.place_forget()

class IpInputScreen():
    def create(self,app):
        self.input_label = Label(app.root,text="Receiver IP Address: ")
        self.input_box = Entry(app.root)
        self.ok_button = Button(app.root, text="Next >",command=lambda: self.handle_next(app))
        self.back_button = Button(app.root, text="< Back",command=lambda: app.change_view(app.ip_input,app.choice_screen))
    
    def handle_next(self,app):
        ip = self.input_box.get()
        flag  = app.handler.check_conn(ip)
        if flag:
            app.send_to_ip = ip
            app.change_view(app.ip_input,app.file_input)  
        else :
            messagebox.showerror(title="Failed", message=f"Connection to {ip} failed")

    def render(self):
        self.input_label.place(relx=0.2,rely=0.5,anchor=CENTER)
        self.input_box.place(relx=0.7,rely=0.5,anchor=CENTER)
        self.ok_button.place(relx=0.8,rely=0.9,anchor=CENTER)
        self.back_button.place(relx=0.5,rely=0.9,anchor=CENTER)
    
    def hide(self):
        self.input_label.place_forget()
        self.input_box.place_forget()
        self.ok_button.place_forget()
        self.back_button.place_forget()

class FileScreen():
    def create(self,app):
        self.file_selected = False
        self.msg_label = Label(app.root,text="Please wait till receiver responds")
        self.input_label = Label(app.root,text="Select a file: ")
        self.browse_button = Button(app.root, text="Browse",command=self.browsefunc)
        self.filepath_label = Label(app.root,text="File not selected")
        self.ok_button = Button(app.root, text="Ok",command=lambda: self.handle_ok(app))
        self.back_button = Button(app.root, text="< Back",command=lambda: app.change_view(app.file_input,app.ip_input))
        self.home_button = Button(app.root, text="Home",command=lambda: app.change_view(app.file_input,app.choice_screen))

    def handle_ok(self,app):
        if(self.file_selected):
            messagebox.showinfo(title="Wait",message="Wait till the receiver responds\nPlease press OK to send the file")
            status = app.handler.handle_send(app.send_to_ip,self.filename)
            if status[0] == True:
                messagebox.showinfo(title="Success",message="File sent successfully")

            if status[0] == False:
                if(status[1] == 405):
                    messagebox.showerror(title="Failed", message="File declined by receiver")
                if(status[1] == 500):
                    messagebox.showerror(title="Failed", message="There was a problem at receiver's end")
                if(status[1] == 404):
                    messagebox.showerror(title="Failed", message="Receiver is not active or invalid file selected")
        else:
            messagebox.showwarning(title="Failed", message="Please select a file to transfer")
    
    def browsefunc(self):
        self.filename = filedialog.askopenfilename()
        if(self.filename != ""):
            self.filepath_label.config(text=self.filename)
            self.file_selected = True
        
        

    def render(self):
        self.input_label.place(relx=0.2,rely=0.5,anchor=CENTER)
        self.browse_button.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.filepath_label.place(relx=0.5,rely=0.7,anchor=CENTER)
        self.ok_button.place(relx=0.8,rely=0.9,anchor=CENTER)
        self.back_button.place(relx=0.5,rely=0.9,anchor=CENTER)
        self.back_button.place(relx=0.3,rely=0.9,anchor=CENTER)

    def hide(self):
        self.browse_button.place_forget()
    
    def get_data(self):
        return self.path_input.get()
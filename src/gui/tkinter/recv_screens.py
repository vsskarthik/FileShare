from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from tkinter import scrolledtext

class ConfirmationScreen:
    def create(self,app):
        self.input_label = Label(app.root,text="Click \"Next\" to start receiving files from sender")
        self.ok_button = Button(app.root, text="Next >",command=lambda: self.handle_next(app))
        self.back_button = Button(app.root, text="< Back",command=lambda: app.change_view(app.conf_screen,app.choice_screen))
    
    def handle_next(self,app):
        app.change_view(app.conf_screen,app.info_screen)
        app.handler.handle_recv("0.0.0.0",2805,app)
        #print("Recv Handler")

    def render(self):
        self.input_label.place(relx=0.1,rely=0.4,anchor=W)
        self.ok_button.place(relx=0.8,rely=0.9,anchor=CENTER)
        self.back_button.place(relx=0.5,rely=0.9,anchor=CENTER)
    
    def hide(self):
        self.input_label.place_forget()
        self.ok_button.place_forget()
        self.back_button.place_forget()

class InfoScreen:
    def create(self,app):
        self.log_box = scrolledtext.ScrolledText(app.root, wrap = WORD, height=10,width=41)
        self.back_button = Button(app.root, text="< Back",command=lambda: self.handle_back(app))

    def handle_back(self,app):
        app.change_view(app.info_screen,app.conf_screen)
    
    def write_info(self,text):
        self.log_box.insert(END, text + '\n')
        #self.log_box.see(END)
    
    def show_error(self,text):
        messagebox.showerror(title="Failed", message=text)
    
    def show_success(self,text):
        messagebox.showinfo(title="Success",message=text)
    
    def get_conf(self,text):
        return messagebox.askyesno(title="Confirmation",message=text)

    def render(self):
        self.log_box.place(relx=0,rely=0)#row=0, column=0, sticky=(N, S, W, E))
        self.back_button.place(relx=0.9,rely=0.9,anchor=E)#row=1, column=1, sticky=(S, E))
        

    def hide(self):
        self.log_box.delete(1.0,END)
        self.log_box.place_forget()
        self.back_button.place_forget()
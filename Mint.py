#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 . , ? ! : ; ' " - _ / \ | ( ) [ ] { } < > + - * / = % & @ # $ ^ ~ `
import tkinter as tk
from tkinter import filedialog



class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.config(padx=20,pady=20)
        self.window.title("Password")
        self.buttons_canvas = tk.Canvas(self.window)

        file_selector_label = tk.Label(self.window, text = "Please select a file:")
        self.file_selection_box = tk.Entry(self.window,width=50)
        self.file_selection_button = tk.Button(self.window, text = "Choose", command = self.choose)
        password_label = tk.Label(self.window,text = "Please type in your password:")
        self.password_entry = tk.Entry(self.window, )
        spacer = tk.Label(self.window, text = " ")
        encrypt_button = tk.Button(self.buttons_canvas, text = "Encrypt", command=self.encrypt_button)
        decrypt_button = tk.Button(self.buttons_canvas, text = "Decrypt", command=self.decrypt_button)

        file_selector_label.grid(column=0,row=0, sticky = "w")
        self.file_selection_box.grid(column=1,row=0)
        self.file_selection_button.grid(column=2,row=0)
        password_label.grid(column=0,row=1, sticky = "w")
        self.password_entry.grid(column = 1, row = 1, columnspan = 2, sticky = "w" + "e")
        spacer.grid(column = 0, row = 2)
        self.buttons_canvas.grid(column = 0, row = 3,sticky = "w")
        encrypt_button.grid(column = 0, row = 0)
        decrypt_button.grid(column = 1, row = 0)

        self.window.mainloop()
    def choose(self):
        path = filedialog.askopenfilename()
        self.file_selection_box.delete(0, tk.END)
        self.file_selection_box.insert(0,path)
        self.file_selection_box.update()

    def check(self):
        item = self.file_selection_box.get()
        if len(item) != 0:
            return True
        else:
            return False

    def encrypt_button(self):
        if self.check():
            pass
        else:
            empty_box()
            # error message TODO

    def decrypt_button(self):
        if self.check():
            pass
        else:
            empty_box()
            # error message TODO


def empty_box():
    window = tk.Tk()
    window.config(padx=20,pady=20)
    window.title("No file path")

    error_label = tk.Label(window, text= "Please select a file to encrypt/decrypt")
    ok_button = tk.Button(window, text= "OK", command = window.destroy)

    error_label.grid(column=0, row=0)
    ok_button.grid(column=0, row=1, sticky="w")

    window.mainloop()




Window()

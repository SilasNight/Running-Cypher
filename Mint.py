#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 . , ? ! : ; ' " - _ / \ | ( ) [ ] { } < > + - * / = % & @ # $ ^ ~ `
import tkinter as tk
from tkinter import filedialog


class Window:
    def __init__(self):
        self.window = tk.Tk()
        self.window.config(padx=20,pady=20)
        self.window.title("Password")

        file_selector_label = tk.Label(self.window, text = "Please select a file:")
        self.file_selection_box = tk.Entry(self.window,width=50)
        self.file_selection_button = tk.Button(self.window, text = "Choose", command = self.choose)
        password_label = tk.Label(self.window,text = "Please type in your password:")
        self.password_entry = tk.Entry(self.window, )
        spacer = tk.Label(self.window, text = " ")
        encrypt_button = tk.Button(self.window, text = "Encrypt", command=self.check)

        file_selector_label.grid(column=0,row=0, sticky = "w")
        self.file_selection_box.grid(column=1,row=0)
        self.file_selection_button.grid(column=2,row=0)
        password_label.grid(column=0,row=1, sticky = "w")
        self.password_entry.grid(column = 1, row = 1, columnspan = 2, sticky = "w" + "e")
        spacer.grid(column = 0, row = 2)
        encrypt_button.grid(column = 0, row = 3, sticky = "w")

        self.window.mainloop()
    def choose(self):
        path = filedialog.askopenfilename()
        self.file_selection_box.delete(0, tk.END)
        self.file_selection_box.insert(0,path)
        self.file_selection_box.update()

    def check(self):
        item = self.file_selection_box.get()
        if len(item) != 0:
            self.encypt()
        else:
            pass
            #error message TODO



Window()

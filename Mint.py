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
        path = self.file_selection_box.get()
        document_type = path[-4:]
        print(document_type)
        if len(path) != 0:
            if document_type != ".txt":
                error("Not a .txt file","The File has to be a .txt")
            else:
                return True
        else:
            error("No file path","Please select a file to encrypt/decrypt")

    def encrypt_button(self):
        if self.check():
            self.encryption("jack")



    def decrypt_button(self):
        if self.check():
            self.encryption("jack")


    def encryption(self,action):
        characters = ['Z', 'K', '(', 'U', '-', 'h', '0', 'X', 'i', 'v', '#', '}', '=', ':', 'w', 'f', '/', '9', '|',
                      'B', 'E', 'N', 'e', ';', 'c', "'", '`', '&', 'd', ']', '1', '<', '-', 'M', '*', ',', '5', 'u',
                      'j', 'C', 'O', '"', 'z', 'W', 'x', '[', 'a', 'b', 'F', 'Q', '?', '@', 'D', '4', 'L', 'q', 'G',
                      'J', 'I', 'y', 'R', 'H', 'o', '+', '%', 'T', 'm', '^', '6', '_', '3', '7', '$', 'V', '2', 'l',
                      'k', 's', '8', 'P', 'Y', 'r', ')', ' ', 'S', '.', '>', '~', 'g', 'n', 'p', 't', '{', '!', 'A']

        password = self.password_entry.get()
        password = list(password)

        for index, char in enumerate(password):
            value = characters.index(char)
            password[index] = value
        print(password)

        path = self.file_selection_box.get()
        with open(path,"r") as file:
            text = file.read()







def error(label,message):
    window = tk.Tk()
    window.config(padx=20,pady=20)
    window.title(label)

    error_label = tk.Label(window, text= message)
    ok_button = tk.Button(window, text= "OK", command = window.destroy)

    error_label.grid(column=0, row=0)
    ok_button.grid(column=0, row=1, sticky="w")

    window.mainloop()




Window()

import tkinter as tk
from tkinter import filedialog


class Window:
    def __init__(self):
        self.characters = [
            'Z', 'K', '(', 'U', '-', 'h', '0', 'X', 'i', 'v', '#', '}', '=', ':', 'w', 'f', '/', '9', '|', 'B', 'E',
            'N', 'e', ';', 'c', "'", '`', '&', 'd', ']', '1', '<', '-', 'M', '*', ',', '5', 'u', 'j', 'C', 'O', '"',
            'z', 'W', 'x', '[', 'a', 'b', 'F', 'Q', '?', '@', 'D', '4', 'L', 'q', 'G', 'J', 'I', 'y', 'R', 'H', 'o',
            '+', '%', 'T', 'm', '^', '6', '_', '3', '7', '$', 'V', '2', 'l', 'k', 's', '8', 'P', 'Y', 'r', ')', ' ',
            'S', '.', '>', '~', 'g', 'n', 'p', 't', '{', '!', 'A', '\n',
        ]

        self.window = tk.Tk()
        self.window.config(padx=20, pady=20)
        self.window.title("Password")
        self.buttons_canvas = tk.Canvas(self.window)

        file_selector_label = tk.Label(self.window, text="Please select a file:")
        self.file_selection_box = tk.Entry(self.window, width=50)
        self.file_selection_button = tk.Button(self.window, text="Choose", command=self.choose)
        password_label = tk.Label(self.window, text="Please type in your password:")
        self.password_entry = tk.Entry(self.window, )
        spacer = tk.Label(self.window, text=" ")
        encrypt_button = tk.Button(self.buttons_canvas, text="Encrypt", command=self.encrypt_button)
        decrypt_button = tk.Button(self.buttons_canvas, text="Decrypt", command=self.decrypt_button)

        file_selector_label.grid(column=0, row=0, sticky="w")
        self.file_selection_box.grid(column=1, row=0)
        self.file_selection_button.grid(column=2, row=0)
        password_label.grid(column=0, row=1, sticky="w")
        self.password_entry.grid(column=1, row=1, columnspan=2, sticky="w" + "e")
        spacer.grid(column=0, row=2)
        self.buttons_canvas.grid(column=0, row=3, sticky="w")
        encrypt_button.grid(column=0, row=0)
        decrypt_button.grid(column=1, row=0)

        self.window.mainloop()

    def choose(self):
        path = filedialog.askopenfilename()
        self.file_selection_box.delete(0, tk.END)
        self.file_selection_box.insert(0, path)
        self.file_selection_box.update()

    def check(self):
        path = self.file_selection_box.get()
        document_type = path[-4:]
        if len(path) != 0:
            if document_type != ".txt":
                error("Not a .txt file", "The File has to be a .txt")
                return False
            else:
                return True
        else:
            error("No file path", "Please select a file to encrypt/decrypt")
            return False

    def encrypt_button(self):
        if self.check():
            self.cypher("encrypt")

    def decrypt_button(self):
        if self.check():
            self.cypher("decrypt")

    def get_path(self):
        path = self.file_selection_box.get()
        return path

    def get_text(self):
        path = self.get_path()

        with open(path, "r") as file:
            text = file.read()
        return text

    def get_text_values(self, text):
        values = []
        for char in text:
            try:
                value = self.characters.index(char)
                values.append(value)
            except ValueError:
                print(char)

        return values

    @staticmethod
    def encrypt_text_values(password, text_values):
        password_length = len(password) - 1

        output = []
        for index, value in enumerate(text_values):
            index %= password_length
            temp_value = value + password[index]
            new_value = temp_value % 95
            output.append(new_value)
        return output

    @staticmethod
    def decrypt_text_values(password, text_values):
        password_length = len(password) - 1

        output = []
        for index, value in enumerate(text_values):
            index %= password_length
            temp_value = value - password[index]
            output.append(temp_value)
        return output

    def text_of_values(self, numbered_values):
        text = ""
        for value in numbered_values:
            character = self.characters[value]
            text += character
        return text

    def save_text(self, text):
        path = self.get_path()

        with open(path, "w") as file:
            file.write(text)

    def cypher(self, action):
        password = self.get_password_value()

        text = self.get_text()

        text_values = self.get_text_values(text)

        if action == "encrypt":
            number_values = self.encrypt_text_values(password, text_values)
        else:
            number_values = self.decrypt_text_values(password, text_values)

        encrypted_text = self.text_of_values(number_values)

        self.save_text(encrypted_text)

        print("Done!")

    def get_password_value(self):
        password = self.password_entry.get()
        password_value = self.get_text_values(password)

        return password_value


def error(label, message):
    window = tk.Tk()
    window.config(padx=20, pady=20)
    window.title(label)

    error_label = tk.Label(window, text=message)
    ok_button = tk.Button(window, text="OK", command=window.destroy)

    error_label.grid(column=0, row=0)
    ok_button.grid(column=0, row=1, sticky="w")

    window.mainloop()


Window()

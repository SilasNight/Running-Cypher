"""
This program is to encrypt text files. Specifically .txt files.
It does this with what can be considered a dual encryption one
of which is a running cypher and the other is a randomized alphabet
to seed from.
"""

import tkinter as tk
from tkinter import filedialog


class Window:
    def __init__(self):
        """
        The main window for tkinter and the setup there of.

        I also put in the randomized alphabet here and not in a function
        so that the alphabet doesn't have to be generated and saved
        over and over again.
        """

        # Randomized list of characters to use as the alphabet
        self.characters = [
            'Z', 'K', '(', 'U', 'h', '0', 'X', 'i', 'v', '#', '}', '=', ':', 'w', 'f', '/', '9', '|', 'B', 'E', '—',
            'N', 'e', ';', 'c', "'", '`', '&', 'd', ']', '1', '<', '-', 'M', '*', ',', '5', 'u', 'j', 'C', 'O', '"',
            'z', 'W', 'x', '[', 'a', 'b', 'F', 'Q', '?', '@', 'D', '4', 'L', 'q', 'G', 'J', 'I', 'y', 'R', 'H', 'o',
            '+', '%', 'T', 'm', '^', '6', '_', '3', '7', '$', 'V', '2', 'l', 'k', 's', '8', 'P', 'Y', 'r', ')', ' ',
            'S', '.', '>', '~', 'g', 'n', 'p', 't', '{', '!', 'A', '\n',
        ]

        # Create the window the user will see
        self.window = tk.Tk()
        self.window.config(padx=20, pady=20)
        self.window.title("Password")
        self.buttons_canvas = tk.Canvas(self.window)

        # Create the components
        file_selector_label = tk.Label(self.window, text="Please select a file:")
        self.file_selection_box = tk.Entry(self.window, width=50)
        self.file_selection_button = tk.Button(self.window, text="Choose", command=self.choose)
        password_label = tk.Label(self.window, text="Please type in your password:")
        self.password_entry = tk.Entry(self.window, )
        spacer = tk.Label(self.window, text=" ")
        encrypt_button = tk.Button(self.buttons_canvas, text="Encrypt", command=self.encrypt_button)
        decrypt_button = tk.Button(self.buttons_canvas, text="Decrypt", command=self.decrypt_button)

        # Place the components
        file_selector_label.grid(column=0, row=0, sticky="w")
        self.file_selection_box.grid(column=1, row=0)
        self.file_selection_button.grid(column=2, row=0)
        password_label.grid(column=0, row=1, sticky="w")
        self.password_entry.grid(column=1, row=1, columnspan=2, sticky="w" + "e")
        spacer.grid(column=0, row=2)
        self.buttons_canvas.grid(column=0, row=3, sticky="w")
        encrypt_button.grid(column=0, row=0)
        decrypt_button.grid(column=1, row=0)

        # Run the window
        self.window.mainloop()

    def choose(self) -> None:
        """
        Edits the dialog box and adds the path of the file chosen
        by the user
        """

        path = filedialog.askopenfilename()
        self.file_selection_box.delete(0, tk.END)
        self.file_selection_box.insert(0, path)
        self.file_selection_box.update()

    def check(self) -> bool:
        """
        Makes sure that the path given to the program is a .txt file
        """

        # Get the path
        path = self.file_selection_box.get()
        document_type = path[-4:]

        # Make sure there is at least something in the path
        if len(path) != 0:

            # Check if that something is a .txt file
            if document_type != ".txt":
                message_box("Not a .txt file", "The File has to be a .txt")
                return False
            else:
                return True
        else:
            message_box("No file path", "Please select a file to encrypt/decrypt")
            return False

    def encrypt_button(self) -> None:
        """
        The function that is run if the encrypt button is clicked
        """

        if self.check():
            self.cypher("encrypt")

    def decrypt_button(self) -> None:
        """
        the function that is called if the decrypt button is clicked
        """

        if self.check():
            self.cypher("decrypt")

    def get_path(self) -> str:
        """
        Gets the string currently in the path text box and returns it
        """

        path = self.file_selection_box.get()
        return path

    def get_text(self) -> str:
        """
        Gets the text out of the text file. And returns it as a string
        """

        path = self.get_path()

        # Read and return the text
        with open(path, "r") as file:
            text = file.read()
        return text

    def text_to_values(self, text: str) -> list:
        """
        Goes through all the characters in the text and compares it to the
        randomized alphabet and gets its index as a value.

        It creates a list of those values and returns it.
        :param text: The text to be changed
        :return: List of values
        """

        values = []
        for char in text:
            value = self.characters.index(char)
            values.append(value)

        return values

    @staticmethod
    def encrypt_text_values(password: list, text_values: list, length: int) -> list:
        """
        Using the passwords values, I run through the text values and increase them.
        By doing so encrypting them with a running cypher.

        :param password: list of password values
        :param text_values: list of text values
        :param length: length of the randomized alphabet
        :return: list of changed text values
        """

        # Get the length of the password to use with modulo
        password_length = len(password)

        output = []

        # Go through each text value and change them and store them
        for index, value in enumerate(text_values):
            index %= password_length
            temp_value = value + password[index]
            new_value = temp_value % length
            output.append(new_value)

        # Return the changed text
        return output

    @staticmethod
    def decrypt_text_values(password: list, text_values: list) -> list:
        """
        Using the passwords values, I run through the text values and increase them.
        By doing so encrypting them with a running cypher.

        Note there is no length. This was used to wrap the encryption so
        that it doesn't go out of the bounds of the alphabet. Negative numbers
        automatically wrap.

        :param password: list of password values
        :param text_values: list of text values
        :return: List of changed values
        """

        # Get password length for modulo
        password_length = len(password)

        output = []

        # Change the text values one by one
        for index, value in enumerate(text_values):
            index %= password_length
            temp_value = value - password[index]
            output.append(temp_value)

        # Return the changed values
        return output

    def values_to_text(self, numbered_values: list) -> str:
        """
        Changes the changed text values back into text.
        :param numbered_values: The changed text values
        :return: string
        """

        # Change the values back into characters and add them to a string
        text = ""
        for value in numbered_values:
            character = self.characters[value]
            text += character

        # Return the string
        return text

    def save_text(self, text: str) -> None:
        """
        Save the changed text back to the file
        :param text: Changed text to be saved
        """

        path = self.get_path()

        # Write to file
        with open(path, "w") as file:
            file.write(text)

    def cypher(self, action: str) -> None:
        """
        The main controlling function to keep things neat.

        :param action: String to tell the function what to do
        """

        # Get the length of the alphabet
        char_list_length = len(self.characters)

        # Get the values of the password
        password = self.get_password_value()

        # Get the text from the text file
        text = self.get_text()

        # Get the values of the text
        text_values = self.text_to_values(text)

        # Increase or decrease the values of the text values based on the
        # button that was clicked
        if action == "encrypt":
            number_values = self.encrypt_text_values(password, text_values, char_list_length)
        else:
            number_values = self.decrypt_text_values(password, text_values)

        # Change those values back into text
        encrypted_text = self.values_to_text(number_values)

        # Save the text back to the file
        self.save_text(encrypted_text)

        # Confirmation message
        if action == "encrypt":
            message_box("Completed!", "Encryption Completed!")
        else:
            message_box("Completed!", "Decryption Completed!")

    def get_password_value(self) -> list:
        """
        Get the typed in password and immediately change it to
        a list of values.
        """

        # Get password
        password = self.password_entry.get()

        # Change to list of values
        password_value = self.text_to_values(password)

        # Return list of values
        return password_value


def message_box(label: str, message: str) -> None:
    """
    Creates a small window to display a message to the user.

    :param label: Title of the box
    :param message: Message in the box
    """

    # Create the window
    window = tk.Tk()
    window.config(padx=20, pady=20)

    # Change title
    window.title(label)

    # Change the message
    message_label = tk.Label(window, text=message)

    ok_button = tk.Button(window, text="OK", command=window.destroy)

    message_label.grid(column=0, row=0)
    ok_button.grid(column=0, row=1, sticky="w")

    window.mainloop()


Window()

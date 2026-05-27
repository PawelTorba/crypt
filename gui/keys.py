import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from algorithms.rsa_signature import generate_keys

class KeysFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.output_private_key_file = None # RSA private key file for signing
        self.output_public_key_file = None # RSA public key file for verifying signature

        ## KEYS FRAME -< main frame
        self.keys_frame = tk.Frame(self)
        self.keys_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        ## KEY OPTIONS DIALOG FRAME -< keys frame
        self.key_options_dialog_frame = tk.Frame(self.keys_frame)
        self.key_options_dialog_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        key_size_label = tk.Label(self.key_options_dialog_frame, text="Rozmiar klucza:")
        key_size_label.grid(row=0, column=0, padx=10, pady=(20 , 5), sticky="w")
        key_sizes = ["1024", "2048", "..."]
        self.selected_key_size = tk.StringVar(value=key_sizes[0])
        key_size_dropdown = ttk.Combobox(
            self.key_options_dialog_frame,
            textvariable=self.selected_key_size,
            values=key_sizes,
            state="readonly",
            width=20
        )
        key_size_dropdown.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")  

        self.keys_file_dialog_frame = tk.Frame(self.keys_frame)
        self.keys_file_dialog_frame.grid(row=2, column=0, columnspan=3, sticky="w")
        self.file_label_private_key = tk.Label(self.keys_file_dialog_frame, text="Plik klucza prywatnego:")
        self.file_label_private_key.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_private_key = tk.Button(self.keys_file_dialog_frame, text="Przeglądaj", command=self.browse_private_key_file)
        self.button_browse_private_key.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.file_label_public_key = tk.Label(self.keys_file_dialog_frame, text="Plik klucza publicznego:")
        self.file_label_public_key.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_public_key = tk.Button(self.keys_file_dialog_frame, text="Przeglądaj", command=self.browse_public_key_file)
        self.button_browse_public_key.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.output_frame_keys = tk.Frame(self.keys_frame)
        self.output_frame_keys.grid(row=3, column=0, columnspan=3, sticky="w")
        self.generate_keys_button = tk.Button(self.output_frame_keys, text="Generuj klucze", width=20, command=self.generate_keys)
        self.generate_keys_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.busy_status_label = tk.Label(self.output_frame_keys, text="Not executed yet")
        self.busy_status_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    def browse_private_key_file(self):
        #browse for private key file target location
        self.output_private_key_file = filedialog.asksaveasfilename()
        if self.output_private_key_file:
            self.file_label_private_key.config(text=f"Plik klucza prywatnego: {self.output_private_key_file}")

    def browse_public_key_file(self):
        #browse for public key file target location
        self.output_public_key_file = filedialog.asksaveasfilename()
        if self.output_public_key_file:
            self.file_label_public_key.config(text=f"Plik klucza publicznego: {self.output_public_key_file}")

    def generate_keys(self):

        try:

            if not self.output_private_key_file or not self.output_public_key_file:
                self.busy_status_label.config(text="Wybierz pliki wyjściowe")
                return

            key_size = int(self.selected_key_size.get())

            generate_keys(
                self.output_private_key_file,
                self.output_public_key_file,
                key_size
            )

            self.busy_status_label.config(text="Klucze wygenerowane")

        except Exception as e:
            self.busy_status_label.config(text=f"Błąd: {e}")
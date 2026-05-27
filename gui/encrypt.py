import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class EncryptFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.input_file = None # file for encryption
        self.output_file = None # file for encrypted output
        self.rsa_key_file_public = None # RSA public key file for encrypting AES key

        ## ENCRYPTION FRAME -< main frame
        self.encrypt_frame = tk.Frame(self)
        self.encrypt_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        ## FILE DIALOG FRAME -< encryption frame
        self.file_dialog_frame = tk.Frame(self)
        self.file_dialog_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        self.file_label_input = tk.Label(self.file_dialog_frame, text="Plik wejściowy:")
        self.file_label_input.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button_browse_input = tk.Button(self.file_dialog_frame, text="Przeglądaj", command=self.browse_input_file)
        self.button_browse_input.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.file_label_output = tk.Label(self.file_dialog_frame, text="Plik wyjściowy:")
        self.file_label_output.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.button_browse_output = tk.Button(self.file_dialog_frame, text="Przeglądaj", command=self.browse_output_file)
        self.button_browse_output.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ## separator
        separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        separator.grid(row=1, column=0, columnspan=10, sticky="ew", padx=10, pady=10)

        ## AES OPTIONS FRAME -< encryption frame
        self.AES_options_frame = tk.Frame(self)
        self.AES_options_frame.grid(row=2, column=0, columnspan=3 , sticky="w")
        self.aes_modes_frame = tk.Frame(self.AES_options_frame)
        self.aes_modes_frame.grid(row=0, column=0, columnspan=3, sticky="w")
        self.label_aes_options = tk.Label(self.aes_modes_frame, text="Tryb AES:")
        self.label_aes_options.grid(row=0, column=0, padx=10, pady=10, sticky="w")  
        self.aes_modes = ["AES-256-CBC", "AES-256-CFB", "AES-256-OFB", "AES-256-CTR"]
        self.selected_aes_mode = tk.StringVar(value=self.aes_modes[0])
        self.aes_mode_dropdown = ttk.Combobox(
            self.aes_modes_frame,
            textvariable=self.selected_aes_mode,
            values=self.aes_modes,
            state="readonly",
            width=20
        )
        self.aes_mode_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="w")  

        self.aes_key_label = tk.Label(self.AES_options_frame, text="Klucz AES:        [Auto-generated]")
        self.aes_key_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.nonce_label = tk.Label(self.AES_options_frame, text="Nonce/IV:        [Auto-generated]")
        self.nonce_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.aes_key_var = tk.BooleanVar(value=True)

        self.aes_key_checkbox = tk.Checkbutton(
            self.AES_options_frame,
            text="Automatycznie generuj klucz AES i nonce/IV",
            variable=self.aes_key_var
        )

        self.aes_key_checkbox.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.aes_key_checkbox.config(state=tk.DISABLED)

        ## separator
        separator2 = ttk.Separator(self, orient=tk.HORIZONTAL)
        separator2.grid(row=3, column=0, columnspan=10, sticky="ew", padx=10, pady=10)

        ## RSA OPTIONS FRAME -< encryption frame
        self.RSA_options_frame = tk.Frame(self)
        self.RSA_options_frame.grid(row=4, column=0, columnspan=3 , sticky="w")
        self.check_rsa_encrypt = tk.Checkbutton(self.RSA_options_frame, text="Szyfruj klucz AES kluczem RSA odbiorcy")
        self.check_rsa_encrypt.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.rsa_public_key_label = tk.Label(self.RSA_options_frame, text="Klucz publiczny RSA odbiorcy:")
        self.rsa_public_key_label.grid(row=1, column=0, padx=10,pady=10, sticky="w")
        self.rsa_public_key_button = tk.Button(self.RSA_options_frame, text="Przeglądaj", command=self.browse_public_rsa_key)
        self.rsa_public_key_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        ## separator
        separator2 = ttk.Separator(self, orient=tk.HORIZONTAL)
        separator2.grid(row=5, column=0, columnspan=10, sticky="ew", padx=10, pady=10)

        ## OUTPUT FRAME -< main frame
        self.output_frame = tk.Frame(self)
        self.output_frame.grid(row=7, column=0, columnspan=3, sticky="w")
        self.encrypt_button = tk.Button(self.output_frame, text="Szyfruj", width=20, command=self.encrypt)
        self.encrypt_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.busy_status_label = tk.Label(self.output_frame, text="Not executed yet")
        self.busy_status_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    def browse_input_file(self):
        #browse for input file to encrypt
        self.input_file = filedialog.askopenfilename()
        if self.input_file:
            self.file_label_input.config(text=f"Plik wejściowy: {self.input_file}")

    def browse_output_file(self):
        #browse for output file to save encrypted data
        self.output_file = filedialog.asksaveasfilename()
        if self.output_file:
            self.file_label_output.config(text=f"Plik wyjściowy: {self.output_file}")

    def browse_public_rsa_key(self):
        #browse for RSA public key file to encrypt AES key
        self.rsa_key_file_public = filedialog.askopenfilename()
        if self.rsa_key_file_public:
            self.rsa_public_key_label.config(text=f"Klucz publiczny RSA odbiorcy: {self.rsa_key_file_public}")

    def encrypt(self):
        #encryption logic will go here
        pass
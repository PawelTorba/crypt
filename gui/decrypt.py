import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class DecryptFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        self.input_file = None # file for decryption
        self.output_file = None   # file for decrypted output
        self.nonce_iv_file = None # file for nonce/IV used in AES decryption
        self.aes_key_file = None # file for AES key)
        self.rsa_key_file_private = None # RSA private key file for decrypting AES key

        ## DECRYPTION FRAME -< main frame
        self.decrypt_frame = tk.Frame(self)
        self.decrypt_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        ## FILE DIALOG FRAME -< decryption frame
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

        ## AES OPTIONS FRAME -< decryption frame
        self.AES_options_frame = tk.Frame(self)
        self.AES_options_frame.grid(row=2, column=0, columnspan=3 , sticky="w")

        self.aes_mode_dropdown_frame = tk.Frame(self.AES_options_frame)
        self.aes_mode_dropdown_frame.grid(row=0, column=0, columnspan=3, sticky="w")
        self.label_aes_options = tk.Label(self.aes_mode_dropdown_frame, text="Tryb AES:")
        self.label_aes_options.grid(row=0, column=0, padx=10, pady=10, sticky="w")  
        self.aes_modes = ["AES-256-CBC", "AES-256-CFB", "AES-256-OFB", "AES-256-CTR"]
        self.selected_aes_mode = tk.StringVar(value=self.aes_modes[0])
        self.aes_mode_dropdown = ttk.Combobox(
            self.aes_mode_dropdown_frame,
            textvariable=self.selected_aes_mode,
            values=self.aes_modes,
            state="readonly",
            width=20
        )
        self.aes_mode_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="w")  
        self.nonce_label = tk.Label(self.AES_options_frame, text="Nonce/IV:")
        self.button_browse_nonce = tk.Button(self.AES_options_frame, text="Przeglądaj", command=self.browse_nonce_iv)
        self.nonce_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_nonce.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        ## separator
        separator2 = ttk.Separator(self, orient=tk.HORIZONTAL)
        separator2.grid(row=3, column=0, columnspan=10, sticky="ew", padx=10, pady=10)


        ## AES KEY OPTIONS FRAME -< decryption frame
        self.AES_key_options_frame = tk.Frame(self)
        self.AES_key_options_frame.grid(row=4, column=0, columnspan=3 , sticky="w")
        self.aes_key_label = tk.Label(self.AES_key_options_frame, text="Klucz AES:")
        self.aes_key_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_aes_key = tk.Button(self.AES_key_options_frame, text="Przeglądaj", command=self.browse_aes_key)
        self.button_browse_aes_key.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.aes_key_var = tk.BooleanVar(value=False)
        self.aes_key_checkbox = tk.Checkbutton(
            self.AES_key_options_frame,
            text="Klucz AES zaszyfrowany kluczem RSA",
            variable=self.aes_key_var
        )
        self.aes_key_checkbox.grid(row=1, column=0, padx=10, pady=10, sticky="w")   

        self.rsa_key_label = tk.Label(self.AES_key_options_frame, text="Klucz prywatny RSA odbiorcy:")
        self.rsa_key_label.grid(row=2, column=0, padx=10,pady=10, sticky="w")
        self.rsa_key_button = tk.Button(self.AES_key_options_frame, text="Przeglądaj", command=self.browse_rsa_private_key)
        self.rsa_key_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")


        ## separator
        separator3 = ttk.Separator(self, orient=tk.HORIZONTAL)
        separator3.grid(row=5, column=0, columnspan=10, sticky="ew", padx=10, pady=10)

        ## OUTPUT FRAME -< main frame
        self.output_frame = tk.Frame(self)
        self.output_frame.grid(row=6, column=0, columnspan=3, sticky="w")
        self.decrypt_button = tk.Button(self.output_frame, text="Odszyfruj", width=20, command=self.decrypt)
        self.decrypt_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.busy_status_label = tk.Label(self.output_frame, text="Not executed yet")
        self.busy_status_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    def browse_input_file(self):
        #browse for input file to decrypt
        self.input_file = filedialog.askopenfilename()
        if self.input_file:
            self.file_label_input.config(text=f"Plik wejściowy: {self.input_file}")

    def browse_output_file(self):
        #browse for output file to save decrypted data
        self.output_file = filedialog.asksaveasfilename()
        if self.output_file:
            self.file_label_output.config(text=f"Plik wyjściowy: {self.output_file}")

    def browse_aes_key(self):
        #browse for AES key file for decryption (if AES key is encrypted with RSA, this will be the encrypted AES key file)
        self.aes_key_file = filedialog.askopenfilename()
        if self.aes_key_file:
            self.aes_key_label.config(text=f"Klucz AES: {self.aes_key_file}")

    def browse_rsa_private_key(self):
        #browse for RSA private key file to decrypt AES key
        self.rsa_key_file_private = filedialog.askopenfilename()
        if self.rsa_key_file_private:
            self.rsa_key_label.config(text=f"Klucz prywatny RSA odbiorcy: {self.rsa_key_file_private}")

    def browse_nonce_iv(self):
        #browse for nonce/IV file for AES decryption
        self.nonce_iv_file = filedialog.askopenfilename()
        if self.nonce_iv_file:
            self.nonce_label.config(text=f"Nonce/IV: {self.nonce_iv_file}")

    def decrypt(self):
        #decryption logic will go here
        pass
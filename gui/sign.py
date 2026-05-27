import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from algorithms.rsa_signature import sign_file, verify_signature

class SignFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #variables for signing
        self.to_sign_file = None # file to sign
        self.private_rsa_key_file = None # RSA private key file for signing
        self.output_file = None # file for signature output

        #variables for verifying signature
        self.rsa_key_file_public = None # RSA public key file for verifying signature
        self.to_verify_file = None # file to verify signature on
        self.signature_file = None # file containing the signature to verify

        ## SIGN FRAME -< main frame
        self.sign_frame = tk.Frame(self)
        self.sign_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        ## SIGN DIALOG FRAME -< sign frame
        self.sign_dialog_frame = tk.Frame(self)
        self.sign_dialog_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        self.file_label_to_sign = tk.Label(self.sign_dialog_frame, text="Plik do podpisu:")
        self.file_label_to_sign.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button_browse_to_sign_file = tk.Button(self.sign_dialog_frame, text="Przeglądaj", command=self.browse_to_sign_file)
        self.button_browse_to_sign_file.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.file_label_rsa_private = tk.Label(self.sign_dialog_frame, text="Klucz prywatny RSA nadawcy:")
        self.file_label_rsa_private.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_rsa_private = tk.Button(self.sign_dialog_frame, text="Przeglądaj", command=self.browse_private_RSA_key)
        self.button_browse_rsa_private.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.file_label_output_signature = tk.Label(self.sign_dialog_frame, text="Plik podpisu:")
        self.file_label_output_signature.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_output = tk.Button(self.sign_dialog_frame, text="Przeglądaj", command=self.browse_output_file)
        self.button_browse_output.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.output_frame_sign = tk.Frame(self.sign_dialog_frame)
        self.output_frame_sign.grid(row=4, column=0, columnspan=3, sticky="w")
        self.sign_button = tk.Button(self.output_frame_sign, text="Podpisz", width=20, command=self.sign)
        self.sign_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.busy_status_label_1 = tk.Label(self.output_frame_sign, text="Not executed yet")
        self.busy_status_label_1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ## separator
        separator = ttk.Separator(self, orient=tk.HORIZONTAL)
        separator.grid(row=1, column=0, columnspan=10, sticky="ew", padx=10, pady=10)

        ## Verify signature DIALOG FRAME -< sign frame
        self.verify_dialog_frame = tk.Frame(self)
        self.verify_dialog_frame.grid(row=2, column=0, columnspan=3, sticky="w")

        self.file_label_to_verify = tk.Label(self.verify_dialog_frame, text="Plik do weryfikacji:")
        self.file_label_to_verify.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button_browse_to_verify_file = tk.Button(self.verify_dialog_frame, text="Przeglądaj", command=self.browse_to_verify_file)
        self.button_browse_to_verify_file.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.file_label_rsa_public = tk.Label(self.verify_dialog_frame, text="Klucz publiczny RSA nadawcy:")
        self.file_label_rsa_public.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_rsa_public = tk.Button(self.verify_dialog_frame, text="Przeglądaj", command=self.browse_public_RSA_key)
        self.button_browse_rsa_public.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.file_label_signature = tk.Label(self.verify_dialog_frame, text="Plik podpisu:")
        self.file_label_signature.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.button_browse_signature_file = tk.Button(self.verify_dialog_frame, text="Przeglądaj", command=self.browse_signature_file)
        self.button_browse_signature_file.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.output_frame_verify = tk.Frame(self.verify_dialog_frame)
        self.output_frame_verify.grid(row=4, column=0, columnspan=3, sticky="w")
        self.verify_button = tk.Button(self.output_frame_verify, text="Zweryfikuj", width=20, command=self.verify_signature)
        self.verify_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.busy_status_label_2 = tk.Label(self.output_frame_verify, text="Not executed yet")
        self.busy_status_label_2.grid(row=0, column=1, padx=10, pady=10, sticky="w")


    def browse_to_sign_file(self):
        #browse for file to sign
        self.to_sign_file = filedialog.askopenfilename()
        if self.to_sign_file:
            self.file_label_to_sign.config(text=f"Plik do podpisania: {self.to_sign_file}")

    def browse_output_file(self):
        self.output_file = filedialog.asksaveasfilename()

        if self.output_file:
            self.file_label_output_signature.config(
                text=f"Plik podpisu: {self.output_file}"
            )

    def browse_public_RSA_key(self):

        self.rsa_key_file_public = filedialog.askopenfilename()

        if self.rsa_key_file_public:
            self.file_label_rsa_public.config(
                text=f"Klucz publiczny RSA nadawcy: {self.rsa_key_file_public}"
            )

    def browse_private_RSA_key(self):

        self.private_rsa_key_file = filedialog.askopenfilename()

        if self.private_rsa_key_file:
            self.file_label_rsa_private.config(
                text=f"Klucz prywatny RSA nadawcy: {self.private_rsa_key_file}"
            )

    def browse_to_verify_file(self):
        #browse for file to verify signature on
        self.to_verify_file = filedialog.askopenfilename()
        if self.to_verify_file:
            self.file_label_to_verify.config(text=f"Plik do weryfikacji: {self.to_verify_file}")

    def browse_signature_file(self):

        self.signature_file = filedialog.askopenfilename()

        if self.signature_file:
            self.file_label_signature.config(
                text=f"Plik podpisu: {self.signature_file}"
            )

    def sign(self):

        try:

            if not self.to_sign_file:
                self.busy_status_label_1.config(text="Wybierz plik")
                return

            if not self.private_rsa_key_file:
                self.busy_status_label_1.config(text="Wybierz klucz prywatny")
                return

            if not self.output_file:
                self.busy_status_label_1.config(text="Wybierz plik podpisu")
                return

            sign_file(
                self.to_sign_file,
                self.private_rsa_key_file,
                self.output_file
            )

            self.busy_status_label_1.config(text="Plik podpisany")

        except Exception as e:
            self.busy_status_label_1.config(text=f"Błąd: {e}")

    def verify_signature(self):

        try:

            if not self.to_verify_file:
                self.busy_status_label_2.config(text="Wybierz plik")
                return

            if not self.rsa_key_file_public:
                self.busy_status_label_2.config(text="Wybierz klucz publiczny")
                return

            if not self.signature_file:
                self.busy_status_label_2.config(text="Wybierz podpis")
                return

            result = verify_signature(
                self.to_verify_file,
                self.rsa_key_file_public,
                self.signature_file
            )

            if result:
                self.busy_status_label_2.config(text="Podpis poprawny")
            else:
                self.busy_status_label_2.config(text="Podpis NIEPOPRAWNY")

        except Exception as e:
            self.busy_status_label_2.config(text=f"Błąd: {e}")
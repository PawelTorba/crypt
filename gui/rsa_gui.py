import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class RSA_FRAME(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.RSA_parameters_frame = tk.Frame(self)
        self.RSA_parameters_frame.grid(row=0, column=0, columnspan=3, sticky="w")

        self.encrypt_mode_frame = tk.Frame(self);  
        self.decrypt_mode_frame = tk.Frame(self); 

        action_label = tk.Label(self.RSA_parameters_frame, text="Action:")
        action_label.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="w")  

        #action buttons
        actions = ["Encrypt", "Decrypt"]
        self.selected_action = tk.StringVar(value=actions[0])
        action_dropdown = ttk.Combobox(
            self.RSA_parameters_frame,
            textvariable=self.selected_action,
            values=actions,
            state="readonly",
            width=20
        )
        action_dropdown.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")    
        self.selected_action.trace_add("write", self.switch_action)

        ##initialaly show encrypt mode
        self.encrypt_mode_frame.grid(row=1, column=0, sticky="w")

        #keysize selection
        keysize_label = tk.Label(self.RSA_parameters_frame, text="Key Size:")
        keysize_label.grid(row=0, column=2, padx=10, pady=(20 , 5), sticky="w")
        key_sizes = ["1024", "2048", "4096"]
        self.selected_keysize = tk.StringVar(value=key_sizes[1])
        keysize_dropdown = ttk.Combobox(
            self.RSA_parameters_frame,
            textvariable=self.selected_keysize,
            values=key_sizes,
            state="readonly",
            width=20
        )
        keysize_dropdown.grid(row=0, column=3, padx=10, pady=(20, 5), sticky="w")    
        #self.selected_keysize.trace_add("write", switch_keysize)

         #padding mode selection
        padding_mode_label = tk.Label(self.RSA_parameters_frame, text="Padding Mode:")
        padding_mode_label.grid(row=1, column=0, padx=10, pady=(20 , 5), sticky="w")
        padding_modes = ["OAEP", "APKCS1v15"]
        self.selected_padding_mode = tk.StringVar(value=padding_modes[0])
        padding_mode_dropdown = ttk.Combobox(
            self.RSA_parameters_frame,
            textvariable=self.selected_padding_mode,
            values=padding_modes,
            state="readonly",
            width=20
        )
        padding_mode_dropdown.grid(row=1, column=1, padx=10, pady=(20, 5), sticky="w")    
        #self.selected_padding_mode.trace_add("write", self.switch_padding_mode)

                    #key entry frame
        self.key_entry_frame = tk.Frame(self.RSA_parameters_frame)
        self.key_entry_frame.grid(row=2, column=0, columnspan=4, sticky="w")
        key_label_public = tk.Label(self.key_entry_frame, text="Public Key:")
        key_label_public.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="w")
        self.key_entry_public = ScrolledText(self.key_entry_frame, width=40, height=5)
        self.key_entry_public.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")   

        key_label_private = tk.Label(self.key_entry_frame, text="Private Key:")
        key_label_private.grid(row=0, column=2, padx=10, pady=(20, 5), sticky="w")
        self.key_entry_private = ScrolledText(self.key_entry_frame, width=40, height=5)
        self.key_entry_private.grid(row=0, column=3, padx=10, pady=(20, 5), sticky="w")

        button_frame_encrypt = tk.Frame(self.key_entry_frame)
        button_frame_encrypt.grid(row=1, column=0, columnspan=4, pady=20)

            #RSA KEY MANAGEMENT BUTTONS
        generate_keys_btn = tk.Button(button_frame_encrypt, text="Generate Key Pair", width=15)
        generate_keys_btn.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="w")
        load_public_key_btn = tk.Button(button_frame_encrypt, text="Load Public Key", width=15)
        load_public_key_btn.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")
        save_public_key_btn = tk.Button(button_frame_encrypt, text="Save Public Key", width=15)
        save_public_key_btn.grid(row=0, column=2, padx=10, pady=(20, 5), sticky="w")
        load_private_key_btn = tk.Button(button_frame_encrypt, text="Load Private Key", width=15)
        load_private_key_btn.grid(row=0, column=3, padx=10, pady=(20, 5), sticky="w")
        save_private_key_btn = tk.Button(button_frame_encrypt, text="Save Private Key", width=15)
        save_private_key_btn.grid(row=0, column=4, padx=10, pady=(20, 5), sticky="w")


        ###ENCRYPT MODE FRAME ###
            #output and input text frames
        self.input_label_text = tk.Label(self.encrypt_mode_frame, text="Input:")
        self.input_label_text.grid(row=1, column=0, padx=10, pady=(20, 5), sticky="w")

        self.input_text = tk.Text(self.encrypt_mode_frame, height=12, width=40)
        self.input_text.grid(row=2, column=0, padx=10, pady=5)

        self.output_label_text = tk.Label(self.encrypt_mode_frame, text="Output:")
        self.output_label_text.grid(row=1, column=1, padx=10, pady=(20, 5), sticky="w")

        self.output_text = tk.Text(self.encrypt_mode_frame, height=12, width=40)
        self.output_text.grid(row=2, column=1, padx=10, pady=5)

        self.output_text.config(state="disabled")

        ###DECRYPT MODE FRAME ###
        self.input_label_text = tk.Label(self.decrypt_mode_frame, text="Input:")
        self.input_label_text.grid(row=1, column=0, padx=10, pady=(20, 5), sticky="w")

        self.input_text = tk.Text(self.decrypt_mode_frame, height=12, width=40)
        self.input_text.grid(row=2, column=0, padx=10, pady=5)

        self.output_label_text = tk.Label(self.decrypt_mode_frame, text="Output:")
        self.output_label_text.grid(row=1, column=2, padx=10, pady=(20, 5), sticky="w")

        self.output_text = tk.Text(self.decrypt_mode_frame, height=12, width=40)
        self.output_text.grid(row=2, column=2, padx=10, pady=5)
        self.output_text.config(state="disabled")


        #### BUTTON FRAME ####
        button_frame = tk.Frame(self)
        button_frame.grid(row=3, column=0, columnspan=3, pady=20)

        action_btn = tk.Button(button_frame, text="Perform Action", width=15)
        action_btn.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        from_file_btn = tk.Button(button_frame, text="From File", width=15)
        from_file_btn.grid(row=1, column=0, padx=10)

        export_btn = tk.Button(button_frame, text="Export to File", width=15)
        export_btn.grid(row=1, column=2, padx=10)

    def switch_action(self, *args):
        # remove all frames
        for frame in (self.encrypt_mode_frame, self.decrypt_mode_frame):
            frame.grid_forget()

        algo = self.selected_action.get()         
        if algo == "Encrypt":
            self.encrypt_mode_frame.grid(row=1, column=0, sticky="w")
        elif algo == "Decrypt":
            self.decrypt_mode_frame.grid(row=1, column=0, sticky="w")
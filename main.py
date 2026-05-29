import gui.encrypt as encrypt
import gui.decrypt as decrypt
import gui.keys as keys
import gui.sign as sign

from tkinter import ttk
import tkinter as tk


root = tk.Tk()
root.title("Encryption / Decryption Tool")
root.geometry("800x600")

# CENTER CONTAINER FRAME
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")


# FRAMES
encrypt_frame = encrypt.EncryptFrame(main_frame)
decrypt_frame = decrypt.DecryptFrame(main_frame)
sign_frame = sign.SignFrame(main_frame)
keys_frame = keys.KeysFrame(main_frame)

main_button_frame = tk.Frame(main_frame)
main_button_frame.grid(row=0, column=0, columnspan=2, pady=20, sticky="w")

main_button_encrypt = tk.Button(main_button_frame, text="Encrypt", width=20, command=lambda: switch_frame(encrypt_frame))
main_button_encrypt.grid(row=0, column=0, padx=10)
main_button_decrypt = tk.Button(main_button_frame, text="Decrypt", width=20, command=lambda: switch_frame(decrypt_frame))
main_button_decrypt.grid(row=0, column=1, padx=10)
main_button_sign = tk.Button(main_button_frame, text="Sign", width=20, command=lambda: switch_frame(sign_frame))
main_button_sign.grid(row=0, column=2, padx=10)
main_button_keys = tk.Button(main_button_frame, text="Keys", width=20, command=lambda: switch_frame(keys_frame))
main_button_keys.grid(row=0, column=3, padx=10)
separator = ttk.Separator(main_button_frame, orient=tk.HORIZONTAL)
separator.grid(row=1, column=0, columnspan=10, sticky="ew", padx=10, pady=10)

encrypt_frame.grid(row=1, column=0, sticky="w")

def switch_frame(frame):
    # remove all frames
    for f in (encrypt_frame, decrypt_frame, sign_frame, keys_frame):
        f.grid_forget()

    frame.grid(row=1, column=0, sticky="w")


root.mainloop()
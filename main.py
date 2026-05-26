import gui.aes_gui as aes_gui
import gui.rsa_gui as rsa_gui
from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Encryption / Decryption Tool")
root.geometry("1440x900")

# CENTER CONTAINER FRAME
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")


# ALGORITHM SELECTOR
aes_frame = aes_gui.AES_FRAME(main_frame)
rsa_frame = rsa_gui.RSA_FRAME(main_frame)

def switch_algo(*args):
    # remove all frames
    for frame in (aes_frame, rsa_frame):
        frame.grid_forget()

    algo = selected_algo.get()

    if algo == "AES":
        aes_frame.grid(row=1, column=0, sticky="w")
    elif algo == "RSA":
        rsa_frame.grid(row=1, column=0, sticky="w")

## SELECTOR FRAME ##
selector_frame = tk.Frame(main_frame)
algo_label = tk.Label(selector_frame, text="Choose encryption algorithm:")
algo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

algorithms = ["AES", "RSA"]

selected_algo = tk.StringVar(value=algorithms[0])

algo_dropdown = ttk.Combobox(
    selector_frame,
    textvariable=selected_algo,
    values=algorithms,
    state="readonly",
    width=20
)
algo_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="w")
selector_frame.grid(row=0, column=0, columnspan=2, sticky="w")
selected_algo.trace_add("write", switch_algo)

root.mainloop()
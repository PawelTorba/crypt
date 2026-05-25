import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Encryption / Decryption Tool")
root.geometry("900x500")

# -----------------------------------
# CENTER CONTAINER FRAME
# -----------------------------------
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor="center")


# -----------------------------------
# ALGORITHM SELECTOR
# -----------------------------------

aes_frame = tk.Frame(main_frame)
rsa_frame = tk.Frame(main_frame)
des_frame = tk.Frame(main_frame)

def switch_algo(*args):
    # remove all frames
    for frame in (aes_frame, rsa_frame, des_frame):
        frame.grid_forget()

    algo = selected_algo.get()

    if algo == "AES":
        aes_frame.grid(row=1, column=0, sticky="w")
    elif algo == "RSA":
        rsa_frame.grid(row=1, column=0, sticky="w")
    elif algo == "DES":
        des_frame.grid(row=1, column=0, sticky="w")

############################
## SELECTOR FRAME CONTENT ##
############################
selector_frame = tk.Frame(main_frame)
algo_label = tk.Label(selector_frame, text="Choose encryption algorithm:")
algo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

algorithms = ["AES", "RSA", "DES", "Caesar Cipher"]

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


############################
## AES FRAME CONTENT      ##
############################
AES_parameters_frame = tk.Frame(aes_frame)
AES_parameters_frame.grid(row=0, column=0, columnspan=3, sticky="w")

action_label = tk.Label(AES_parameters_frame, text="Action:")
action_label.grid(row=0, column=0, padx=10, pady=(20, 5), sticky="w")

#action buttons
actions = ["Encrypt", "Decrypt"]
selected_action = tk.StringVar(value=actions[0])
action_dropdown = ttk.Combobox(
    AES_parameters_frame,
    textvariable=selected_action,
    values=actions,
    state="readonly",
    width=20
)
action_dropdown.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")    
#selected_action.trace_add("write", switch_action)

#keysize selection
keysize_label = tk.Label(AES_parameters_frame, text="Key Size:")
keysize_label.grid(row=1, column=0, padx=10, pady=(20 , 5), sticky="w")
key_sizes = ["128", "192", "256"]
selected_keysize = tk.StringVar(value=key_sizes[0])
keysize_dropdown = ttk.Combobox(
    AES_parameters_frame,
    textvariable=selected_keysize,
    values=key_sizes,
    state="readonly",
    width=20
)
keysize_dropdown.grid(row=1, column=1, padx=10, pady=(20, 5), sticky="w")    
#selected_keysize.trace_add("write", switch_keysize)

#chain mode selection
chain_mode_label = tk.Label(AES_parameters_frame, text="Chain Mode:")
chain_mode_label.grid(row=2, column=0, padx=10, pady=(20 , 5), sticky="w")
chain_modes = ["ECB", "CBC", "CFB", "OFB", "CTR"]
selected_chain_mode = tk.StringVar(value=chain_modes[0])
chain_mode_dropdown = ttk.Combobox(
    AES_parameters_frame,
    textvariable=selected_chain_mode,
    values=chain_modes,
    state="readonly",
    width=20
)
chain_mode_dropdown.grid(row=2, column=1, padx=10, pady=(20, 5), sticky="w")    
#selected_chain_mode.trace_add("write", switch_chain_mode)

# -----------------------------------
# INPUT TEXT (LEFT)
# -----------------------------------
input_label = tk.Label(aes_frame, text="Input:")
input_label.grid(row=3, column=0, padx=10, pady=(20, 5), sticky="w")

input_text = tk.Text(aes_frame, height=12, width=40)
input_text.grid(row=4, column=0, padx=10, pady=5)

# -----------------------------------
# OUTPUT TEXT (RIGHT)
# -----------------------------------
output_label = tk.Label(aes_frame, text="Output:")
output_label.grid(row=3, column=1, padx=10, pady=(20, 5), sticky="w")

output_text = tk.Text(aes_frame, height=12, width=40)
output_text.grid(row=4, column=1, padx=10, pady=5)

output_text.config(state="disabled")






# -----------------------------------
# BOTTOM BUTTONS
# -----------------------------------
button_frame = tk.Frame(aes_frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=20)

action_btn = tk.Button(button_frame, text="Perform Action", width=15)
action_btn.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

from_file_btn = tk.Button(button_frame, text="From File", width=15)
from_file_btn.grid(row=1, column=0, padx=10)

export_btn = tk.Button(button_frame, text="Export to File", width=15)
export_btn.grid(row=1, column=1, padx=10)

root.mainloop()
import tkinter as tk
import winsound
from pathlib import Path

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
TITLE_COLORS = ("#79E8FF", "#FFE17A", "#FF93D2")


def shift_block(block, steps):
    shifted = ""
    for char in block:
        position = SYMBOLS.index(char)
        new_position = (position + steps) % len(SYMBOLS)
        shifted += SYMBOLS[new_position]
    return shifted


def generate_key():
    first = first_entry.get().strip().upper()
    if len(first) != 5 or any(char not in SYMBOLS for char in first):
        key_text.set("Invalid input")
        return

    second = shift_block(first, 3)
    third = shift_block(first, -5)
    key_text.set(f"{first}-{second}-{third}")


def convert_hex():
    hex_number = hex_entry.get().strip()
    try:
        dec = int(hex_number, 16)
        dec_text.set(str(dec))
    except ValueError:
        dec_text.set("Invalid HEX")


def animate_title(index=0):
    title.config(fg=TITLE_COLORS[index])
    root.after(700, animate_title, (index + 1) % len(TITLE_COLORS))


root = tk.Tk()
root.title("Lab 3 - Key Generator (Variant 5)")
root.geometry("760x440")
root.resizable(False, False)

# Game background
background_image = tk.PhotoImage(file=str(Path(__file__).with_name("background.png")))
background = tk.Label(root, image=background_image)
background.place(x=0, y=0)

# Main panel
panel = tk.Frame(root, bg="#10243e", padx=17, pady=12)
panel.place(x=371, y=9, width=357, height=422)

title = tk.Label(panel, text="KEY GENERATOR", font=("Arial", 17, "bold"),
                 fg="white", bg="#10243e")
title.pack(pady=(0, 10))

instruction = tk.Label(panel, text="Enter 5 characters (A-Z, 0-9):",
                       fg="white", bg="#10243e")
instruction.pack(pady=(0, 5))

first_entry = tk.Entry(panel, font=("Consolas", 14), justify="center")
first_entry.pack(pady=(0, 8))

button = tk.Button(panel, text="Generate", command=generate_key,
                   font=("Arial", 11))
button.pack(pady=(0, 8))

result_label = tk.Label(panel, text="Generated key:", fg="white", bg="#10243e")
result_label.pack(pady=(0, 5))

key_text = tk.StringVar()
result_entry = tk.Entry(panel, textvariable=key_text, state="readonly",
                        font=("Consolas", 13), justify="center", width=23)
result_entry.pack(pady=(0, 10))

# HEX to DEC conversion
separator = tk.Frame(panel, bg="#507091", height=1)
separator.pack(fill="x", pady=(0, 10))

hex_label = tk.Label(panel, text="HEX to DEC (example: 1A = 26)",
                     fg="white", bg="#10243e")
hex_label.pack(pady=(0, 5))

hex_entry = tk.Entry(panel, font=("Consolas", 13), justify="center")
hex_entry.pack(pady=(0, 7))

convert_button = tk.Button(panel, text="Convert", command=convert_hex,
                           font=("Arial", 11))
convert_button.pack(pady=(0, 7))

dec_label = tk.Label(panel, text="Decimal number:", fg="white", bg="#10243e")
dec_label.pack(pady=(0, 5))

dec_text = tk.StringVar()
dec_entry = tk.Entry(panel, textvariable=dec_text, state="readonly",
                     font=("Consolas", 13), justify="center")
dec_entry.pack()

# Change the title color every 700 milliseconds
animate_title()

# Loop the background music on Windows
winsound.PlaySound(
    str(Path(__file__).with_name("music.wav")),
    winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP
)

root.mainloop()

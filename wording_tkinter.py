
import tkinter as tk
from tkinter import ttk
import pyttsx3

# Function to handle hundreds, tens, and units
def hnd(n1, n2, n3, m):
    ls0 = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
    ls1 = ["Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
    ls2 = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
    ls3 = ["", "Hundred ", "Thousand ", "Million ", "Billion ", "Trillion "]

    if n1 == 0 and n2 == 1:
        w = ls1[n3] + ls3[m]
    elif n1 == 0 and n2 > 1:
        w = ls2[n2] + ls0[n3] + ls3[m]
    elif n1 == 0 and n2 == 0 and n3 == 0:
        w = ""
    else:
        w = ls0[n3] + ls3[m]

    if n1 >= 1 and n2 == 1:
        w = ls0[n1] + ls3[1] + ls1[n3] + ls3[m]
    elif n1 >= 1 and n2 > 1:
        w = ls0[n1] + ls3[1] + ls2[n2] + ls0[n3] + ls3[m]
    elif n1 >= 1 and n2 == 0:
        w = ls0[n1] + ls3[1] + ls0[n3] + ls3[m]
    else:
        None

    return w

# Function to convert numbers to words
def inWords(ns):
    nn = list(ns.strip())[::-1]
    i = len(nn)
    while i < 15:
        nn.append("0")
        i += 1
    nn1 = [ord(n) - 48 for n in nn]
    nn = nn1[::-1]
    nw = (
        hnd(nn[0], nn[1], nn[2], 5)
        + hnd(nn[3], nn[4], nn[5], 4)
        + hnd(nn[6], nn[7], nn[8], 3)
        + hnd(nn[9], nn[10], nn[11], 2)
        + hnd(nn[12], nn[13], nn[14], 0)
    )
    return nw

# Function to handle button click and display input text
def display_text():
    num = input_entry.get()
    if not num.isdigit() or len(num) > 15:
        output_label.config(text="Please enter a valid number up to 15 digits.")
    else:
        wording = inWords(num)
        output_label.config(text=wording)

# Function to handle text-to-speech
def speak_text():
    num = input_entry.get()
    if not num.isdigit() or len(num) > 15:
        output_label.config(text="Please enter a valid number up to 15 digits.")
    else:
        wording = inWords(num)
        speech = pyttsx3.init()
        speech.say(wording)
        speech.runAndWait()

# Function to copy the result to clipboard with auto-reset message
def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(output_label.cget("text"))
    app.update()
    status_label.config(text="Copied to clipboard!")
    app.after(2000, lambda: status_label.config(text=""))

# Function to save the result to a file
def save_to_file():
    num = input_entry.get()
    if not num.isdigit() or len(num) > 15:
        output_label.config(text="Please enter a valid number up to 15 digits.")
    else:
        wording = inWords(num)
        with open("number_in_words.txt", "w") as file:
            file.write(wording)
        status_label.config(text="Saved to 'number_in_words.txt'")
        

# Create the main application window
app = tk.Tk()
app.title("Number to Words Converter")

# Enable resizing
app.geometry("800x600")  # Set initial size
app.state("zoomed")  # Start in maximized mode
app.resizable(True, True)  # Allow resizing

# Configure styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TEntry", font=("Helvetica", 14))

# Main Frame
main_frame = ttk.Frame(app, padding=20)
main_frame.pack(fill="both", expand=True)

# Title Label
title_label = ttk.Label(main_frame, text="Convert Numbers to Figures", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

# Input Section
input_label = ttk.Label(main_frame, text="Enter a Number:")
input_label.pack(anchor="w", pady=5)
input_entry = ttk.Entry(main_frame, width=50)
input_entry.pack(fill="x", pady=5)

# Output Section
output_label = ttk.Label(main_frame, text="", anchor="center", wraplength=750, relief="sunken", padding=10)
output_label.pack(pady=10)

# Button Section
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)

display_button = ttk.Button(button_frame, text="Convert", command=display_text)
display_button.grid(row=0, column=0, padx=15, pady=10)

speak_button = ttk.Button(button_frame, text="Speak", command=speak_text)
speak_button.grid(row=0, column=1, padx=15, pady=10)

copy_button = ttk.Button(button_frame, text="Copy", command=copy_to_clipboard)
copy_button.grid(row=1, column=0, padx=15, pady=10)

save_button = ttk.Button(button_frame, text="Save", command=save_to_file)
save_button.grid(row=1, column=1, padx=15, pady=10)

# Status Label
status_label = ttk.Label(app, text="", anchor="center", foreground="green", font=("Helvetica", 12))
status_label.pack(side="bottom", pady=10)

# Start the GUI main loop
app.mainloop()

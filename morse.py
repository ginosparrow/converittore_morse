import tkinter as tk
import customtkinter as ttk

def clear():
    entry_morse.delete('1.0', tk.END)
    entry_nt.delete('1.0', tk.END)

MORSE_TO_TEXT = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i',
    '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0'
}

TEXT_TO_MORSE = {v: k for k, v in MORSE_TO_TEXT.items()}
TEXT_TO_MORSE[' '] = '/'  # Separator for words


def morse_lettere(text):
    words = text.strip().split(' ')
    for code in words:
        entry_nt.insert(tk.END, MORSE_TO_TEXT.get(code, ''))

def lettere_morse(text):
    for char in text.strip().lower():
        if char == ' ':
            entry_nt.insert(tk.END, '/ ')
        else:
            entry_nt.insert(tk.END, TEXT_TO_MORSE.get(char, '') + ' ')

def coonvert():
    entry_nt.delete('1.0', tk.END)
    text = entry_morse.get("1.0", "end").strip()
    if all(ch in ['.', '-', ' ', '\n'] for ch in text):
        morse_lettere(text)
    else:
        lettere_morse(text)

# UI Setup
ttk.set_appearance_mode("System")
ttk.set_default_color_theme("green")

app = ttk.CTk()
app.geometry("720x480")
app.title("Convertitore Morse")

titolo = ttk.CTkLabel(app, text="Convertitore Morse", text_color="blue")
titolo.configure(font=("Bahnschrift", 20))
titolo.pack(padx=10, pady=10)

griglia = ttk.CTkFrame(app)

griglia.rowconfigure(3)
griglia.columnconfigure(2)

title_morse = ttk.CTkLabel(griglia, text="Text")
title_morse.configure(font=("Bahnschrift", 15))
title_morse.grid(row=0, column=0, padx=10, pady=10)

entry_morse = ttk.CTkTextbox(griglia, width=200, height=200, border_color="blue", border_spacing=3, font=("Arial", 20))
entry_morse.grid(row=1, column=0, padx=10, pady=10)

title_nt = ttk.CTkLabel(griglia, text="Convert Text")
title_nt.configure(font=("Bahnschrift", 15))
title_nt.grid(row=0, column=1, padx=10, pady=10)

entry_nt = ttk.CTkTextbox(griglia, width=200, height=200, border_color="blue", border_spacing=3, font=("Arial", 20))
entry_nt.grid(row=1, column=1, padx=10, pady=10)

b_chek = ttk.CTkButton(griglia, text="Convert", command=coonvert)
b_chek.grid(row=2, column=0, pady=10)

clear_button = ttk.CTkButton(griglia, text="Clear", fg_color="red", command=clear)
clear_button.grid(row=2, column=1, pady=10)

griglia.pack(padx=10, pady=10)

app.mainloop()

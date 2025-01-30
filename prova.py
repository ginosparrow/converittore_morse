import tkinter as tk
import customtkinter as ttk

# Funzione per cancellare il contenuto delle caselle di testo
def clear():
    entry_daconvertire.delete('1.0', tk.END)  # Cancella il testo nella casella di input
    entry_convertito.delete('1.0', tk.END)    # Cancella il testo nella casella di output

# Funzione per convertire da codice Morse a testo normale
def morse_lettere(lettere):
    # Dizionario per mappare il codice Morse ai caratteri
    morse_to_char = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
        '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0'
    }
    
    inp = lettere.strip()  # Rimuove gli spazi iniziali e finali
    words = inp.split(' / ')  # Divide le parole basate su "/"
    
    for word in words:
        letters = word.split()  # Divide i singoli codici Morse
        for letter in letters:
            # Inserisce il carattere corrispondente nel testo di output
            entry_convertito.insert(tk.END, morse_to_char.get(letter, '?'))
        entry_convertito.insert(tk.END, ' ')  # Aggiunge uno spazio tra le parole

# Funzione per convertire da testo normale a codice Morse
def lettere_morse(lettere):
    # Dizionario per mappare i caratteri al codice Morse
    char_to_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----'
    }
    
    inp = lettere.strip().upper()  # Converte il testo in maiuscolo e rimuove spazi
    for char in inp:
        if char == ' ':  # Aggiunge "/" per separare le parole
            entry_convertito.insert(tk.END, ' / ')
        elif char in char_to_morse:
            # Inserisce il codice Morse corrispondente
            entry_convertito.insert(tk.END, char_to_morse[char] + ' ')
        else:
            # Inserisce un punto interrogativo per caratteri non riconosciuti
            entry_convertito.insert(tk.END, '? ')

# Funzione per determinare il tipo di conversione
def converter():
    stecca = entry_daconvertire.get('1.0', tk.END).strip()  # Ottiene il testo di input
    entry_convertito.delete('1.0', tk.END)  # Cancella il testo precedente
    if stecca.startswith('.') or stecca.startswith('-'):
        # Se il testo inizia con "." o "-", converte da Morse a testo
        morse_lettere(stecca)
    else:
        # Altrimenti, converte da testo a Morse
        lettere_morse(stecca)

#------------------------------------------------------------------------------

# Configurazione dell'interfaccia grafica
ttk.set_appearance_mode("System")  # Imposta il tema dell'app
ttk.set_default_color_theme("green")  # Imposta il tema dei colori

app = ttk.CTk()  # Crea la finestra principale
app.geometry("720x480")  # Imposta la dimensione della finestra
app.title("Convertitore Morse")  # Titolo della finestra

# Titolo principale
titolo = ttk.CTkLabel(app, text="Convertitore Morse", text_color="blue")
titolo.configure(font=("Bahnschrift", 20))
titolo.pack(padx=10, pady=10)

# Creazione della griglia per organizzare gli elementi
griglia = ttk.CTkFrame(app)
griglia.rowconfigure(3)
griglia.columnconfigure(2)

# Etichetta per la casella di input
title_daconvertire = ttk.CTkLabel(griglia, text="Da convertire")
title_daconvertire.configure(font=("Bahnschrift", 15))
title_daconvertire.grid(row=0, column=0, padx=10, pady=10)

# Casella di input per il testo o codice Morse
entry_daconvertire = ttk.CTkTextbox(griglia, width=200, height=200, border_color="blue", border_spacing=3, font=("Arial", 20))
entry_daconvertire.grid(row=1, column=0, padx=10, pady=10)

# Etichetta per la casella di output
title_convertito = ttk.CTkLabel(griglia, text="Convertito ")
title_convertito.configure(font=("Bahnschrift", 15))
title_convertito.grid(row=0, column=1, padx=10, pady=10)

# Casella di output per il testo convertito
entry_convertito = ttk.CTkTextbox(griglia, width=200, height=200, border_color="blue", border_spacing=3, font=("Arial", 20))
entry_convertito.grid(row=1, column=1, padx=10, pady=10)

# Bottone per eseguire la conversione
b_chek = ttk.CTkButton(griglia, text="Click", command=converter)
b_chek.grid(row=2, column=0, pady=10)

# Bottone per cancellare le caselle di testo
clear_button = ttk.CTkButton(griglia, text="Clear", fg_color="red", command=clear)
clear_button.grid(row=2, column=1, pady=10)

# Mostra la griglia nella finestra
griglia.pack(padx=10, pady=10)

# Avvio dell'applicazione
def main():
    app.mainloop()

if __name__ == "__main__":
    main()

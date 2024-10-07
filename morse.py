import  tkinter as tk
import customtkinter as ttk

def clear():
    entry_morse.delete('1.0', tk.END)
    entry_nt.delete('1.0', tk.END)
    
def morse_lettere(text):
    A = ['.','-']
    B = ['-','.','.','.']
    C = ['-','.','-','.']
    D = ['-','.','.']
    E = ['.' ]
    F = ['.','.','-','.']
    G = ['-','-','.']
    H = ['.','.','.','.']
    I = ['.','.']
    J = ['.','-','-','-']
    K = ['-','.','-'] 
    L = ['.','-','.','.']
    M = ['-','-']
    N = ['-','.']
    O = ['-','-','-']
    P = ['.','-','-','.']
    Q = ['-','-','.','-']
    R = ['.','-','.']
    S = ['.','.','.']
    T = ['-']
    U = ['.','.','-']
    V = ['.','.','.','-']
    W = ['.','-','-']
    X = ['-','.','.','-']
    Y = ['-','.','-','-']
    Z = ['-','-','.','.']
    uno = ['.','-','-','-','-']
    due = ['.','.','-','-','-']
    tre = ['.','.','.','-','-']
    quattro = ['.','.','.','.','-']
    cinque = ['.','.','.','.','.']
    sei = ['-','.','.','.','.']
    sette = ['-','-','.','.','.']
    otto = ['-','-','-','.','.']
    nove = ['-','-','-','-','.']
    zero = ['-','-','-','-','-']

    parola= []
    index = 0
    inp = text

    def traduttore(p):
        if p == A:
            entry_nt.insert( tk.END, 'a')
        elif p == B:
            entry_nt.insert( tk.END, 'b')
        elif p == C:
            entry_nt.insert( tk.END, 'c')
        elif p == D:
            entry_nt.insert( tk.END, 'd')
        elif p == E:
            entry_nt.insert( tk.END, 'e')
        elif p == F:
            entry_nt.insert( tk.END, 'f')
        elif p == G:
            entry_nt.insert( tk.END, 'g')
        elif p == H:
            entry_nt.insert( tk.END, 'h')
        elif p == I:
            entry_nt.insert( tk.END, 'i')
        elif p == J:
            entry_nt.insert( tk.END, 'j')
        elif p == K:
            entry_nt.insert( tk.END, 'k')
        elif p == L:
            entry_nt.insert( tk.END, 'l')
        elif p == M:
            entry_nt.insert( tk.END, 'm')
        elif p == N:
            entry_nt.insert( tk.END, 'n')
        elif p == O:
            entry_nt.insert( tk.END, 'o')
        elif p == P:
            entry_nt.insert( tk.END, 'p')
        elif p == Q:
            entry_nt.insert( tk.END, 'q')
        elif p == R:
            entry_nt.insert( tk.END, 'r')
        elif p == S:
            entry_nt.insert( tk.END, 's')
        elif p == T:
            entry_nt.insert( tk.END, 't')
        elif p == U:
            entry_nt.insert( tk.END, 'u')
        elif p == V:
            entry_nt.insert( tk.END, 'v')
        elif p == W:
            entry_nt.insert( tk.END, 'w')
        elif p == X:
            entry_nt.insert( tk.END, 'x')
        elif p == Y:
            entry_nt.insert( tk.END, 'y')
        elif p == Z:
            entry_nt.insert( tk.END, 'z')
        elif p == uno:
            entry_nt.insert( tk.END, '1')
        elif p == due:
            entry_nt.insert( tk.END, '2')
        elif p == tre:
            entry_nt.insert( tk.END, '3')
        elif p == quattro:
            entry_nt.insert( tk.END, '4')
        elif p == cinque:
            entry_nt.insert( tk.END, '5')
        elif p == sei:
            entry_nt.insert( tk.END, '6')
        elif p == sette:
            entry_nt.insert( tk.END, '7')
        elif p == otto:
            entry_nt.insert( tk.END, '8')
        elif p == nove:
            entry_nt.insert( tk.END, '9')
        elif p == zero:
            entry_nt.insert( tk.END, '0')

    #print(inp)

    for i in inp:
        
        if i == '/' or i == ' ' or i == "\n":
            #print(' ')
            #print(parola)
            traduttore(parola)
            index = 0
        else:
            parola [index:] = i
            index = index +1
            
    #print(parola)

    #traduttore(parola)

def lettere_morse(text):
    A = '.-'
    B = '-...'
    C = '-.-.'
    D = '-..'
    E = '.'
    F = '..-.'
    G = '--.'
    H = '....'
    I = '..'
    J = '.---'
    K = '-.-'
    L = '.-..'
    M = '--'
    N = '-.'
    O = '---'
    P = '.--.'
    Q = '--.-'
    R = '.-.'
    S = '...'
    T = '-'
    U = '..-'
    V = '...-'
    W = '.--'
    X = '-..-'
    Y = '-.--'
    Z = '--..'
    uno = '.----'
    due = '..---'
    tre = '...--'
    quattro = '....-'
    cinque = '.....'
    sei = '-....'
    sette = ' --...'
    otto = '---..'
    nove = '----.'
    zero = '-----'


    inpp = text

    for ar in inpp :
                entry_morse.insert(tk.END, " ")
                match ar.lower():
                        case 'a':
                            print(A)
                            entry_morse.insert(tk.END, A)
                        case 'b':
                            print(B)
                            entry_morse.insert(tk.END, B)
                        case 'c':
                            print(C)
                            entry_morse.insert(tk.END, C)
                        case 'd':
                            print(D)
                            entry_morse.insert(tk.END, D)
                        case 'e':
                            print(E)
                            entry_morse.insert(tk.END, E)
                        case 'f':
                            print(F)
                            entry_morse.insert(tk.END, F)
                        case 'g':
                            print(G)
                            entry_morse.insert(tk.END, G)
                        case 'h':
                            print(H)
                            entry_morse.insert(tk.END, H)
                        case 'i':
                            print(I)
                            entry_morse.insert(tk.END, I)
                        case 'j':
                            print(J)
                            entry_morse.insert(tk.END, J)
                        case 'k':
                            print(K)
                            entry_morse.insert(tk.END, K)
                        case 'l':
                            print(L)
                            entry_morse.insert(tk.END, L)
                        case 'm':
                            print(M)
                            entry_morse.insert(tk.END, M)
                        case 'n':
                            print(N)
                            entry_morse.insert(tk.END, N)
                        case 'o':
                            print(O)
                            entry_morse.insert(tk.END, O)
                        case 'p':
                            print(P)
                            entry_morse.insert(tk.END, P)
                        case 'q':
                            print(Q)
                            entry_morse.insert(tk.END, Q)
                        case 'r':
                            print(R)
                            entry_morse.insert(tk.END, R)
                        case 's':
                            print(S)
                            entry_morse.insert(tk.END, S)
                        case 't':
                            print(T)
                            entry_morse.insert(tk.END, T)
                        case 'u':
                            print(U)
                            entry_morse.insert(tk.END, U)
                        case 'v':
                            print(V)
                            entry_morse.insert(tk.END, V)
                        case 'w':
                            print(W)
                            entry_morse.insert(tk.END, W)
                        case 'x':
                            print(X)
                            entry_morse.insert(tk.END, X)
                        case 'y':
                            print(Y)
                            entry_morse.insert(tk.END, Y)
                        case 'z':
                            print(Z)
                            entry_morse.insert(tk.END, Z)
                        case " ":
                            entry_morse.insert(tk.END, '/')
                        case "\n":
                            entry_morse.insert(tk.END, "\n")
                        case "1":
                            entry_morse.insert(tk.END, uno)
                        case "2":
                            entry_morse.insert(tk.END, due) 
                        case "3":
                            entry_morse.insert(tk.END, tre)
                        case "4":
                            entry_morse.insert(tk.END, quattro)
                        case "5":
                            entry_morse.insert(tk.END, cinque)
                        case "6":
                            entry_morse.insert(tk.END, sei)
                        case "7":
                            entry_morse.insert(tk.END, sette)
                        case "8":
                            entry_morse.insert(tk.END, otto)
                        case "9":
                            entry_morse.insert(tk.END, nove)
                        case "0":
                            entry_morse.insert(tk.END, zero)
                        case _:
                            entry_morse.insert(tk.END, ar)

def coonvert():
    morsee = entry_morse.get("1.0", "end")
    ntt = entry_nt.get("1.0", "end")

    #if morsee == '' and ntt != '':
    lettere_morse(ntt)
    #elif ntt == '' and morsee != '':
    morse_lettere(morsee)

ttk.set_appearance_mode("System")
ttk.set_default_color_theme("green")

app = ttk.CTk()
app.geometry("720x480")
app.title("Convertitore Morse")

titolo = ttk.CTkLabel(app, text= "Convertitore Morse", text_color="blue")
titolo.configure(font=("Bahnscrift", 20))
titolo.pack(padx= 10, pady=10)

griglia = ttk.CTkFrame(app)

griglia.rowconfigure(3)
griglia.columnconfigure(2)

title_morse = ttk.CTkLabel(griglia, text="Morse")
title_morse.configure(font=("Bahnscrift", 15))
title_morse.grid(row=0, column= 0, padx = 10, pady= 10)

entry_morse = ttk.CTkTextbox(griglia, width=200, height=200, border_color="blue", border_spacing=3, font= ("Arial", 20))
entry_morse.grid(row=1, column= 0, padx = 10, pady= 10)

title_nt = ttk.CTkLabel(griglia, text="Normal Text")
title_nt.configure(font=("Bahnscrift", 15))
title_nt.grid(row=0, column= 1, padx = 10, pady= 10)

entry_nt = ttk.CTkTextbox(griglia, width=200, height=200, border_color="blue", border_spacing=3, font= ("Arial", 20))
entry_nt.grid(row=1, column= 1, padx = 10, pady= 10)

b_chek = ttk.CTkButton(griglia, text="clik", command=coonvert)
b_chek.grid(row= 2, column=0, pady= 10)

clear_button = ttk.CTkButton(griglia, text="clear", fg_color= "red", command= clear)
clear_button.grid(row= 2, column=1, pady = 10)

griglia.pack(padx= 10, pady=10)

app.mainloop()
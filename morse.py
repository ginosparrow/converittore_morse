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
        elif  p == "/":
            entry_nt.insert( tk.END, ' ')

    #print(inp)
    
    for i in inp:
        
        ##if i == ' ' or i == "\n":
            #print(' ')
            #print(parola)
            ##parola [index:] = i
            ##traduttore(parola)
            ##if i == "\n":
                ##parola [index:] = i
                ##index += 1
               ## traduttore(parola)

            ##index = 0 
 
        ##else:
        
        if i == ' ' or i == "\n":
            traduttore(parola)
            index = 0
            if i == "\n":
                entry_nt.insert( tk.END, '\n')
             
        else:
            parola [index:] = i
            index += 1
            
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
                entry_nt.insert(tk.END, " ")
                match ar.lower():
                        case 'a':
                            print(A)
                            entry_nt.insert(tk.END, A)
                        case 'b':
                            print(B)
                            entry_nt.insert(tk.END, B)
                        case 'c':
                            print(C)
                            entry_nt.insert(tk.END, C)
                        case 'd':
                            print(D)
                            entry_nt.insert(tk.END, D)
                        case 'e':
                            print(E)
                            entry_nt.insert(tk.END, E)
                        case 'f':
                            print(F)
                            entry_nt.insert(tk.END, F)
                        case 'g':
                            print(G)
                            entry_nt.insert(tk.END, G)
                        case 'h':
                            print(H)
                            entry_nt.insert(tk.END, H)
                        case 'i':
                            print(I)
                            entry_nt.insert(tk.END, I)
                        case 'j':
                            print(J)
                            entry_nt.insert(tk.END, J)
                        case 'k':
                            print(K)
                            entry_nt.insert(tk.END, K)
                        case 'l':
                            print(L)
                            entry_nt.insert(tk.END, L)
                        case 'm':
                            print(M)
                            entry_nt.insert(tk.END, M)
                        case 'n':
                            print(N)
                            entry_nt.insert(tk.END, N)
                        case 'o':
                            print(O)
                            entry_nt.insert(tk.END, O)
                        case 'p':
                            print(P)
                            entry_nt.insert(tk.END, P)
                        case 'q':
                            print(Q)
                            entry_nt.insert(tk.END, Q)
                        case 'r':
                            print(R)
                            entry_nt.insert(tk.END, R)
                        case 's':
                            print(S)
                            entry_nt.insert(tk.END, S)
                        case 't':
                            print(T)
                            entry_nt.insert(tk.END, T)
                        case 'u':
                            print(U)
                            entry_nt.insert(tk.END, U)
                        case 'v':
                            print(V)
                            entry_nt.insert(tk.END, V)
                        case 'w':
                            print(W)
                            entry_nt.insert(tk.END, W)
                        case 'x':
                            print(X)
                            entry_nt.insert(tk.END, X)
                        case 'y':
                            print(Y)
                            entry_nt.insert(tk.END, Y)
                        case 'z':
                            print(Z)
                            entry_nt.insert(tk.END, Z)
                        case " ":
                            entry_nt.insert(tk.END, '/')
                        case "\n":
                            entry_nt.insert(tk.END, "\n")
                        case "1":
                            entry_nt.insert(tk.END, uno)
                        case "2":
                            entry_nt.insert(tk.END, due) 
                        case "3":
                            entry_nt.insert(tk.END, tre)
                        case "4":
                            entry_nt.insert(tk.END, quattro)
                        case "5":
                            entry_nt.insert(tk.END, cinque)
                        case "6":
                            entry_nt.insert(tk.END, sei)
                        case "7":
                            entry_nt.insert(tk.END, sette)
                        case "8":
                            entry_nt.insert(tk.END, otto)
                        case "9":
                            entry_nt.insert(tk.END, nove)
                        case "0":
                            entry_nt.insert(tk.END, zero)
                        case _:
                            entry_nt.insert(tk.END, ar)

def coonvert():
    morsee = entry_morse.get("1.0", "end")
    for i in morsee:
        if i == "-" or i == ".":
            morse_lettere(morsee)
        else:
            lettere_morse(morsee)

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
#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox# componente della libreria per le finestre di allarme 
#import ttkbootstrap as ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Morse')
        self.geometry('400x300')

        self.container = tk.Frame(self)#contenitore principale
        self.container.pack(fill= tk.BOTH, expand= True)#creazione del contenitore ceh riempie tutta larea disponibile 

        self.container.grid_rowconfigure(0, weight=1)#creata una griglia 
        self.container.grid_columnconfigure(0, weight=1)
        
        self.page1 = Page1(self.container, self)
        self.page1.grid(row=0, column = 0, sticky='nsew')

        self.page2 = Page2(self.container, self)
        self.page2.grid(row=0, column = 0, sticky='nsew')

        self.page3 = Page3(self.container, self)
        self.page3.grid(row=0, column = 0, sticky='nsew')

        self.show_frame(0)#funzione che permette di mostrare la pagina 1

    def show_frame(self, n):#funzionene che permette di spostarsi da pagina a pagina
        if n == 0:
            self.page1.tkraise()
        elif n == 1:
            self.page2.tkraise()
        elif n == 2:
             self.page3.tkraise()


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['background']= '#fff'
        label = tk.Label(self, text="Lettere a Morse", font= 24,bg='#fff',fg='#ff1111')
        label.pack(padx=10, pady=10)

        sotto_insieme = tk.Frame(self, bg='#fff')
        sotto_insieme.pack()
        sotto_insieme.grid_rowconfigure(0, weight=1)
        sotto_insieme.grid_columnconfigure(2, weight=1)

        bt = tk.Button(sotto_insieme, text="Morse a Lettere", bg='#ff2222', border= 0, fg='#fff',font=20, command= lambda: controller.show_frame(1))
        bt.grid(row=0, column=0, padx=10, pady=10)

        bt2 = tk.Button(sotto_insieme, text="INFO",bg='#ff2222', border= 0, fg='#fff', font=20, command= lambda: controller.show_frame(2))
        bt2.grid(row=0, column=1, padx=10, pady=10)

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

        morse = []# array per 

        def calcolo(*args):#converte lettere in codice morse
            n = 0

            try: 
                n = str(a.get())
                n.lower()    
                
                if len(morse) >= 1 and len(n) == 0:#quado vengono cancelati le leltere e non ce ne sono più ninete  viene pulito anche la secoda casela di testo 
                    morse.clear()

                match n[len(n)-1]:
                    case 'a':
                            morse.append(A)
                    case 'b':
                            morse.append(B)
                    case 'c':
                            morse.append(C)##return C
                    case 'd':
                            morse.append(D)##return D
                    case 'e':
                            morse.append(E)##return E
                    case 'f':
                            morse.append(F)
                            ##return F
                    case 'g':
                            morse.append(G)
                            ##return G
                    case 'h':
                            morse.append(H)##return H
                    case 'i':
                            morse.append(I)##return I
                    case 'j':
                            morse.append(J)##return J
                    case 'k':
                            morse.append(K)#return K
                    case 'l':
                            morse.append(L)#return L
                    case 'm':
                            morse.append(M)#return M
                    case 'n':
                            morse.append(N)#return N
                    case 'o':
                            morse.append(O)#return O
                    case 'p':
                            morse.append(P)#return P
                    case 'q':
                            morse.append(Q)#return Q
                    case 'r':
                            morse.append(R)#return R
                    case 's':
                            morse.append(S)#return S
                    case 't':
                            morse.append(T)#return T
                    case 'u':
                            morse.append(U)#return U
                    case 'v':
                            morse.append(V)#return V
                    case 'w':
                            morse.append(W)#return W
                    case 'x':
                            morse.append(X)#return X
                    case 'y':
                            morse.append(Y)#return Y
                    case 'z':
                            morse.append(Z)#return Z

                    case 'A':
                            morse.append(A)
                    case 'B':
                            morse.append(B)
                    case 'C':
                            morse.append(C)##return C
                    case 'D':
                            morse.append(D)##return D
                    case 'E':
                            morse.append(E)##return E
                    case 'F':
                            morse.append(F)
                            ##return F
                    case 'G':
                            morse.append(G)
                            ##return G
                    case 'H':
                            morse.append(H)##return H
                    case 'I':
                            morse.append(I)##return I
                    case 'J':
                            morse.append(J)##return J
                    case 'K':
                            morse.append(K)#return K
                    case 'L':
                            morse.append(L)#return L
                    case 'M':
                            morse.append(M)#return M
                    case 'N':
                            morse.append(N)#return N
                    case 'O':
                            morse.append(O)#return O
                    case 'P':
                            morse.append(P)#return P
                    case 'Q':
                            morse.append(Q)#return Q
                    case 'R':
                            morse.append(R)#return R
                    case 'S':
                            morse.append(S)#return S
                    case 'T':
                            morse.append(T)#return T
                    case 'U':
                            morse.append(U)#return U
                    case 'V':
                            morse.append(V)#return V
                    case 'W':
                            morse.append(W)#return W
                    case 'X':
                            morse.append(X)#return X
                    case 'Y':
                            morse.append(Y)#return Y
                    case 'Z':
                            morse.append(Z)#return Z
                    case ' ':
                            morse.append('/')
                
                if len(morse) != len(n):#controlla chel le lungesse sono diverse se cio e vero togli egli ultimi caratteri quto e la differenza 
                    for i in range(len(morse) -len(n)):
                            morse.pop()

                #print(n)
                #print(morse)
                            

            except:
                n = 'null'

            b.set(morse)
            


        

        a = tk.StringVar()
        a.trace('w', calcolo)#viene intercetato cio che vinene digitsto e inivato alla funzione calcolo 
        b = tk.StringVar()
        #b.trace('w', calcolo2)

        tx1 = tk.Entry(self, textvariable= a, font=50,borderwidth=1, relief= 'solid')

        tx1.focus()
        tx1.pack()

        tx2 = tk.Entry(self, textvariable= b, font='50', borderwidth=1, relief= 'solid')
        tx2.pack(padx=10, pady=10)
        #tx2 = tk.Text(self, textvariable= b)
        #tx2.pack(padx=10, pady=10)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['background']= '#fff'
        label = tk.Label(self, text="Morse a Lettere",font= 24,bg='#fff',fg='#ff1111')
        label.pack(padx=10, pady=10)
        sotto_insieme = tk.Frame(self, bg='#fff')
        sotto_insieme.pack()
        sotto_insieme.grid_rowconfigure(0, weight=1)
        sotto_insieme.grid_columnconfigure(2, weight=1)
        bt = tk.Button(sotto_insieme, text="Lettere a Morse",bg='#ff2222', border= 0, fg='#fff',font=20, command= lambda: controller.show_frame(0))
        bt.grid(row=0, column=0, padx=10, pady=10)
        bt2 = tk.Button(sotto_insieme, text="INFO",bg='#ff2222', border= 0, fg='#fff',font=20, command= lambda: controller.show_frame(2))
        bt2.grid(row=0, column=1, padx=10, pady=10)

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

        parole = []
        frase = []
        old_frase = []
        
        def calcolo(*args):
                n = 0

                try: 
                        frase.clear()
                        b.set("")
                        n = a.get()
                        #print(n)
                        for i in n:
                                #print(i)
                                if  i == ' ' :
                                        #parole.pop()
                                        if parole == A:
                                                frase.append('A')
                                        elif parole == B:
                                                frase.append('B')
                                        elif parole == C:
                                                frase.append('C')
                                        elif parole == D:
                                                frase.append('D')
                                        elif parole == E:
                                                frase.append('E')
                                        elif parole == F:
                                                frase.append('F')
                                        elif parole == G:
                                                frase.append('G')
                                        elif parole == H:
                                                frase.append('H')
                                        elif parole == I:
                                                frase.append('I')
                                        elif parole == J:
                                                frase.append('J')
                                        elif parole == K:
                                                frase.append('K')
                                        elif parole == L:
                                                frase.append('L')
                                        elif parole == M:
                                                frase.append('M')
                                        elif parole == N:
                                                frase.append('N')
                                        elif parole == O:
                                                frase.append('O')
                                        elif parole == P:
                                                frase.append('P')
                                        elif parole == Q:
                                                frase.append('Q')
                                        elif parole == R:
                                                frase.append('R')
                                        elif parole == S:
                                                frase.append('S')
                                        elif parole == T:
                                                frase.append('T')
                                        elif parole == U:
                                                frase.append('U')
                                        elif parole == V:
                                                frase.append('V')
                                        elif parole == W:
                                                frase.append('W')
                                        elif parole == X:
                                                frase.append('X')
                                        elif parole == Y:
                                                frase.append('Y')
                                        elif parole == Z:
                                                frase.append('Z')
                                        
                                        parole.clear()
                                        #print(frase)
                                        b.set(frase)
                                elif i == '/':
                                        frase.append('\n')
                                        
                                else:   
                                        if len(parole) != len(n):
                                                for i in range(len(parole) -len(n)):
                                                        parole.pop()
                                        
                                        parole.append(i)
                                        #print(parole)
                                
                                        
                
                except:
                        n = 'null'

                
                parole.clear()
        

        a = tk.StringVar()
        a.trace('w', calcolo)
        b = tk.StringVar()
        #b.trace('w', calcolo2)

        tx1 = tk.Entry(self, textvariable= a, font=50, borderwidth=1, relief= 'solid')

        tx1.focus()
        tx1.pack()

        tx2 = tk.Entry(self, textvariable= b, font=50, borderwidth=1, relief= 'solid')
        tx2.pack(pady= 10)


class Page3(tk.Frame):
    

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self['background']= '#fff'
        label = tk.Label(self, text="INFO",font= 24,bg='#fff',fg='#ff1111')
        label.pack()
        sotto_insieme = tk.Frame(self, bg='#fff')
        sotto_insieme.pack()
        sotto_insieme.grid_rowconfigure(0, weight=1)
        sotto_insieme.grid_columnconfigure(2, weight=1)
        bt = tk.Button(sotto_insieme, text="Lettere a Morse", bg='#ff2222', border= 0, fg='#fff',font=20, command= lambda: controller.show_frame(0))
        bt.grid(row=0, column=0, padx=10, pady= 10)
        bt2 = tk.Button(sotto_insieme, text="Morse a Lettere",bg='#ff2222', border= 0, fg='#fff',font=20, command= lambda: controller.show_frame(1))
        bt2.grid(row=0, column=1, padx= 10, pady= 10)

        def on_press(event):
             if((event.x >= 18-10 or event.x <= 18+10 )and (event.y >= 130-20 or event.y <= 130+20)):
                    messagebox.showinfo(title= "easterEgg", message="Ora Gino e arrabbito")

        info = tk.Label(self, text= "Ciao untete!:).\n Mi presento, sono Gino colui che ha sritto questo programma.\n Non sai quanto sono contetno che tu stia usando il mio progetto.\n Lunica cosa che ti chiedo e di non usare il codice che ho scrito\n per usi impropi o di dire che l'hai scritto tu Grazie.\n per il resto senti ti libero di usarlo ma non toccare il coniglio.\n Buon lavoro :P\n {\_/}\n ( °.°)\n /><\\",
                        width=50, height=20, justify= 'left', anchor='n')
        info.bind("<Button-1>", on_press)
        info.pack()
    

if __name__ == "__main__":
    app = App()
    app.mainloop()


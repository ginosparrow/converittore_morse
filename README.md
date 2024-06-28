# Convertittore di codice Morse
Molto semplicemente questo programma permette di convertire una frase o parola in codece morse o viceversa. 

## esempio
    ciao mondo
----------------------------
    -.-. .. .- --- / -- --- -. -.. ---

## come funziona ?🤔

Partiamo con La componete grafica viene gestita dalla libreria Tkinter. Questa è gia presente appena installato pytohn 🐍. La versione consilgiata e la 3.11.9 . Se si vuole usare dei preset grafici per Tkinter si puo installare la libreria _ttkbootstrap_.
    
    pip install ttkbootstrap

La conversione da lettere a codice morse, usa una fuzione che fa riferimento a variabili nominate con la lettere contenete il corrispettivo in morse.

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

tutto cio che viene digitato nella casella di testo viene inviata alla funzione 

    def calcolo(*args):

poi viene covnetita da lettera in morse con la funzione match

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
                    ...

in  fine viene retituito il risultato che viene scrita su una casella di testo  

     b.set(morse)

tutti cio si ripete anche per la coverisione da morse a lettere

--------------------
## installazione 🛠
Non serve instalare nulla! tranne python🐍 ovviamnte 😅, ma facoltativamente si puo installare anche la libreria _ttkbootstrap_ totalmente a propia discrezione.

### os suportati

| os|stato di supporto|
|----------|---|
|Linux | ✅ |
| windows |  ✅ |
| Macos | ✅ |

Se si vuole redere i file .exe queidi eseguiblili come una applicazione seguire i passagi per il sistema operativo d'uso utilitario.

### Linux 
Per i sitemi Linux inseriamo al inizio del file python queta stringa di codice

     #!/usr/bin/env python3

ciò permette di redere il file exeguibile senza dover pasare per l'interprete python.

Poi bisogna dargli i permessi di eseguzione 

    chmod +x /percorso/completo/al/tuo/script/nome del tuo 
    script.py

Ora basta creare il file .desktop per avere un launcer cioè un lanciatore della applicazione  (l'icone sul desktop)

    ini
    [Desktop Entry]
    Version=1.0
    Name=MyApp
    Comment=Descrizione della mia applicazione
    Exec=/percorso/completo/al/tuo/script/nome del tuo 
    script.py
    Icon=/percorso/completo/alla/tua/icona.png
    Terminal=false  
    Type=Application
    Categories=Utility;Application;

anche a questo file bisogna dare i permessi di eseguzione

    chmod +x /percorso/completo/a/nome defl file .desktop

Congraturlazione ora facendo un click sul file realizato prima comparia l'icona della vostra applicazoipne e clicandoci sopra si avviera.👍 

### windows
vi bastera installare la libreria pyinstaller 

    pip install pyinstaller

è molto semplice basta seguire la guida online 

### Macos

anche qui basta installare la libreria py2app

    pip install py2app

sepre seguire la guida online 

--------------------
 ## Bene ora puo divertirit a scrivere in morse 
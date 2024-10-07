# Convertittore di codice Morse
Molto semplicemente questo programma permette di convertire una frase o parola in codece morse o viceversa. 

## esempio
    ciao mondo
----------------------------
    -.-. .. .- --- / -- --- -. -.. ---

## come funziona ?🤔
La componete grafica viene gestita dalla libreria Tkinter. Questa è gia presente appena installato pytohn 🐍. La versione consilgiata e la 3.11.9. In questo progetto e stato utilizata una libreria grafiaca aggiuntiva per Tkinter per dargli un'aspetto più gradevole, per non far sebrare la finesta datata (anche se ha il suo fascino).La libreria in questione e TTKBOOTSTRAP.
    
    pip install ttkbootstrap

--------------------
## installazione 🛠
Non serve instalare nulla! tranne python🐍 ovviamnte 😅 e la libreria _ttkbootstrap_ totalmente a propia discrezione.

### os suportati

| os|stato di supporto|
|----------|---|
|Linux | ✅ |
| windows |  ✅ |
| Macos | ✅ |

Se si vuole redere i file .exe queidi eseguiblili come una applicazione, seguire i passagi per il sistema operativo d'uso utilitario.

### Linux 
Per i sitemi Linux inseriamo al inizio del file python queta stringa di codice

     #!/usr/bin/env python3

ciò permette di redere il file ricniamabile dal terminale senza dover pasare per l'interprete python.

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

è molto semplice basta seguire la ['guida online'](https://pyinstaller.org/en/stable/)

### Macos

anche qui basta installare la libreria py2app

    pip install py2app

sepre seguire la ['guida online'](https://py2app.readthedocs.io/en/latest/)

--------------------
 ## Bene ora puo divertirit a scrivere in morse 
from Tkinter import *


def salvafile(nomefile, testofile):

    if nomefile != 'none':
        nuovofile = open(nomefile, 'w')
        nuovofile.write(testofile )
        nuovofile.close
        conferma()

def leggifile(nomefile):
    global stato
    stato = nomefile
    boxcentrale.delete('1.0',END)
    with open(nomefile) as file:
        corpofile = file.readlines()
        for i in range(len(corpofile)):
            if i == 0:
                boxcentrale.insert(END, corpofile[i], 'big')
            else:
                boxcentrale.insert(END, corpofile[i], 'Normale')
    
    

def funzioneBottone1():
    #testo2 = Label(finestra, text="hai cliccato sul bottone", fg="blue", font=("Helvetica", 18)).pack()
    #salvafile("bottone1.txt", contenuto.get())
    leggifile('martedi.txt')

def funzioneBottone2():
    leggifile('giovedi.txt')

def funzioneBottone3():
    leggifile('sabato.txt')

def funzionetastosalva():
    salvafile(stato, boxcentrale.get('1.0',END))

def resetbox():
    global stato
    stato = 'none'
    boxcentrale.delete('1.0',END)
    titolo = 'Segli giorno \n\n'
    quote = 'Clicca sul giorno per visualizzare/modificare'
    boxcentrale.insert(END, titolo, 'big')
    boxcentrale.insert(END, quote, 'Normale')

def conferma():
    global stato
    stato = 'none'
    boxcentrale.delete('1.0',END)
    titolo = 'OK, Ordine Salvato! \n\n'
    quote = 'Clicca sul giorno per visualizzare/modificare'
    boxcentrale.insert(END, titolo, 'big')
    boxcentrale.insert(END, quote, 'Normale')


def annula():
    resetbox()


#VARIABILE AMBIENTE
stato = 'none'



#crea finestre
finestra = Tk()

#Assegna le dimensioni di una finestra
finestra.geometry('400x400+500+200')
finestra.title('Ordini Mozzarelle')  # titolo

# Aggiunge un laber alla form e con la funzione pack la centra
testo = Label(finestra, text='Software per ordini mozzarella', fg='blue', font=('Helvetica', 18)).grid(row=0,columnspan=3)
bottone1 = Button(text='MARTEDI', command=funzioneBottone1).grid(row=1,column=0)
bottone2 = Button(text='GIOVEDI', command=funzioneBottone2).grid(row=1,column=1)
bottone3 = Button(text='SABATO', command=funzioneBottone3).grid(row=1,column=2)

#Crea casella di test
#contenuto = StringVar()
#casella_testo = Entry(finestra, textvariable=contenuto).grid(row=2,columnspan=3 )
#contenuto.set("scegli un ordine dai tasti sopra..")



#Crea TEXT BOX
boxcentrale = Text(finestra, height=18, width=50, background='#f0ffff')
boxcentrale.grid(row=3,columnspan=3)
boxcentrale.tag_configure('big', font=('Verdana', 14, 'bold'))
boxcentrale.tag_configure('Normale', font=('Verdana', 12))
resetbox()



#creazione tasto salva
bottonesalva = Button(text=' SALVA ', command=funzionetastosalva).grid(row=4,columnspan=3)


#creazione tasto annulla
bottonesalva = Button(text='ANNULLA', command=resetbox).grid(row=5,columnspan=3)


#Avvia la form
finestra.mainloop()


 




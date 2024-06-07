import random
from tkinter import *
window = Tk()
window.geometry("500x500")
txt = Entry(window)
txt.place(x=170, y=410)
score = 0
timeleft = 90
Phrases = ['Es ist gut', 'Es ist sehr nett', 'Es ist sehr prima', 'Meine Eltern ist gut', 'Der Hund', 'Die Katze']


lbl = Label(window, text="Welcome to the Typing Game!", fg='black', font=('Times', 30))
lbl.place(x=1, y=1)
lblscore = Label(window, text="Score: ", fg='black', font=('Times', 25))
lblscore.place(x=190, y=50)
lbltime = Label(window, text="Timer: ", fg='black', font=('Times', 25))
lbltime.place(x=190, y=90)
lblphrases = Label(window, text=str(Phrases[0]), bg='white', font=('Times', 30))
lblphrases.place(x=160, y=200)

def Starting(event):
    global timeleft
    if timeleft == 90:
        countdown()
    NextPhrase()

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        lbltime.config(text="Timer: " + str(timeleft))
        lbltime.after(1000, countdown)

def NextPhrase():
    global score
    global timeleft
    if timeleft > 0:
        if txt.get().lower() == Phrases[0].lower():
            score += 1
        txt.delete(0, END)
        random.shuffle(Phrases)
        lblscore.config(text="Score: " + str(score))
        lblphrases.config(text=Phrases[0])


window.bind('<Return>', Starting)
window.mainloop()
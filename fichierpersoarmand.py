import tkinter as tk
from tkinter import *
from tkinter import ttk
from fonctionsclass import *
from dictionnaires import *



def lancer():
    fenetre0 = tk.Tk()
    fenetre0.title("Première fenêtre")
    fenetre0.geometry("300x200")

    photo = PhotoImage(file="glob.avif")

    canvas = Canvas(fenetre,width=350, height=200)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()

    boutton_start = tk.Button(fenetre0, text="commencer le QCM", command = lambda: ouvrir())
    boutton_start.pack(pady=10) # lambda sert a preciser dans quelle fenetre on se trouve (c'est un argument)

#ouvrir
def ouvrir(fenetre="fenetre1", dico=DictioQCM):
    
    i = int(fenetre[-1])
    assert i < 11, "Fin du QCM"
    rep = liste_rep(dico, i)
    quest = liste_quest(dico)

    # Création de la fenetre
    fenetre = tk.Tk()
    fenetre.title("Question "+str(i))
    fenetre.geometry("300x200")

    #!!!!!!!!afficher le drapeau de quest[i-1]
    texte_fenetre = tk.Label(fenetre, text="Quel est le pays de ce drapeau ?")
    texte_fenetre.pack(pady=10)

    # Boutons réponses
    for k in range(4):
        tk.Radiobutton(fenetre, text=rep[k]).pack

    
    # Bouton pour valider
    boutton_valider = tk.Button(fenetre, text="Valider", command=lambda: ouvrir("fenetre"+str(i+1), dico))   #demander au prof pk ça marche pas
    boutton_valider.pack(pady=10) # lambda sert a preciser dans quelle fenetre on se trouve (c'est un argument)

    fenetre.mainloop()


"""
rep1 = Radiobutton(fenetre, text="Quel est le drapeau de ce pays ?")
rep1.pack

rep2 = Radiobutton(fenetre, text="Quel est le drapeau de ce pays ?")
rep2.pack

rep3 = Radiobutton(fenetre, text="Quel est le drapeau de ce pays ?")
rep3.pack

rep4 = Radiobutton(fenetre, text="Quel est le drapeau de ce pays ?")
rep4.pack

fenetre.destroy()

    tk.Checkbutton(fenetre, text="Option 1").pack()
    tk.Checkbutton(fenetre, text="Option 2").pack()
    tk.Checkbutton(fenetre, text="Option 3").pack()
    tk.Checkbutton(fenetre, text="Option 4").pack()
    
"""

ouvrir()
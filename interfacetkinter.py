import tkinter as tk
from tkinter import *
from tkinter import ttk
from fonctionsclass import *
from dictionnaires import *
from PILE import image, ImageTk



def lancer():
    CQCM = Questionnairetressimple()
    fenetre = tk.Tk()
    fenetre.title("Première fenêtre")
    fenetre.geometry("300x200")

    photo = PhotoImage(file="glob.avif")

    canvas = Canvas(fenetre,width=350, height=200)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()

    boutton_start = tk.Button(fenetre, text="commencer le QCM", command = lambda: ouvrir())
    boutton_start.pack(pady=10) # lambda sert a preciser dans quelle fenetre on se trouve (c'est un argument)

# ouvrir
def ouvrir(fenetre="fenetre1", dico=DictioQCM):
    
    i = int(fenetre[-1])
    assert i < 11, "Fin du QCM"
    rep = CQCM.liste_rep(i, dico)
    quest = CQCM.liste_quest(dico)
    fenetre.destroy()


    # Création de la fenetre
    fenetre = tk.Tk()
    fenetre.title("Question "+str(i))
    fenetre.geometry("300x200")


    # question
    texte_fenetre = tk.Label(fenetre, text="Quel est le pays de ce drapeau ?")
    texte_fenetre.pack(pady=10)

    drapeau = Image.open(quest[i-1])
    drapeau = drapeau.resize((200, 200))
    photo = ImageTk.PhotoImage(drapeau)

    image = cannevasImg.create_image(124, 131, image=photo)
    cannevasImg.grid(row=1, column=3, rowspan=4, padx=10, pady=10, sticky=W)

    # Boutons réponses
    for k in range(4):
        tk.Radiobutton(fenetre, text=rep[k]).pack

    
    # Bouton pour valider
    boutton_valider = tk.Button(fenetre, text="Valider", command=lambda: ouvrir("fenetre"+str(i+1), dico))   #demander au prof pk ça marche pas
    boutton_valider.pack(pady=10) # lambda sert a preciser dans quelle fenetre on se trouve (c'est un argument)

    fenetre.mainloop()

import tkinter as tk
from tkinter import *





# Première fenêtre
fenetre1 = tk.Tk()
fenetre1.title("Première fenêtre")
fenetre1.geometry("300x200")

texte_fenetre1= tk.Label(fenetre1, text="Première fenêtre")
texte_fenetre1.pack(pady=10)

tk.Checkbutton(fenetre1, text="Option 1").pack()
tk.Checkbutton(fenetre1, text="Option 2").pack()
tk.Checkbutton(fenetre1, text="Option 3").pack()
tk.Checkbutton(fenetre1, text="Option 4").pack()

# Bouton pour valider
boutton_premier_valider = tk.Button(fenetre1, text="Valider", command=lambda: ouvrir_deuxieme_fenetre(fenetre1))
boutton_premier_valider.pack(pady=10) # lambda sert a preciser dans quelle fenetre on se trouve (c'est un argument)

fenetre1.mainloop()

def ouvrir_deuxieme_fenetre(fenetre_actuelle):
    fenetre_actuelle.destroy()

    fenetre2 = tk.Tk()
    fenetre2.title("Deuxième fenêtre")
    fenetre2.geometry("300x200")

    texte_fenetre2= tk.Label(fenetre2, text="Deuxième fenêtre")
    texte_fenetre2.pack(pady=10)

    tk.Checkbutton(fenetre2, text="Option 1").pack()
    tk.Checkbutton(fenetre2, text="Option 2").pack()
    tk.Checkbutton(fenetre2, text="Option 3").pack()
    tk.Checkbutton(fenetre2, text="Option 4").pack()

    # Bouton pour aller à la 3e fenêtre
    boutton_deux_valider = tk.Button(fenetre2, text="Suivant", command=lambda: ouvrir_troisieme_fenetre(fenetre2))
    boutton_deux_valider.pack(pady=10)

    fenetre2.mainloop()


def ouvrir_troisieme_fenetre(fenetre_actuelle):
    fenetre_actuelle.destroy()

    fenetre3 = tk.Tk()
    fenetre3.title("Troisième fenêtre")
    fenetre3.geometry("300x200")

    texte_fenetre3 = tk.Label(fenetre3, text="Bienvenue dans la troisième fenêtre !")
    texte_fenetre3.pack(pady=20)

    tk.Checkbutton(fenetre3, text="Option 1").pack()
    tk.Checkbutton(fenetre3, text="Option 2").pack()
    tk.Checkbutton(fenetre3, text="Option 3").pack()
    tk.Checkbutton(fenetre3, text="Option 4").pack()

    boutton_trois_valider = tk.Button(fenetre3, text="Suivant", command=lambda: ouvrir_quatrieme_fenetre(fenetre3))
    boutton_trois_valider.pack(pady=10)

    fenetre3.mainloop()

def ouvrir_quatrieme_fenetre(fenetre_actuelle):
    fenetre_actuelle.destroy()

    fenetre4 = tk.Tk()
    fenetre4.title("quatrieme fenêtre")
    fenetre4.geometry("300x200")

    texte_fenetre4 = tk.Label(fenetre4, text="Bienvenue dans la quatrieme fenêtre !")
    texte_fenetre4.pack(pady=20)

    tk.Checkbutton(fenetre4, text="Option 1").pack()   # le .pack est collé derrière le checkbutton pour éviter de remettre une variable
    tk.Checkbutton(fenetre4, text="Option 2").pack()
    tk.Checkbutton(fenetre4, text="Option 3").pack()
    tk.Checkbutton(fenetre4, text="Option 4").pack()

    bouton_quitter = tk.Button(fenetre4, text="Quitter", command=exit)
    bouton_quitter.pack(pady=10)

def ouvrir_troisieme_fenetre(fenetre_actuelle):
    fenetre_actuelle.destroy()

    fenetre3 = tk.Tk()
    fenetre3.title("Troisième fenêtre")
    fenetre3.geometry("300x200")

    texte_fenetre3 = tk.Label(fenetre3, text="Bienvenue dans la troisième fenêtre !")
    texte_fenetre3.pack(pady=20)

    tk.Checkbutton(fenetre3, text="Option 1").pack()
    tk.Checkbutton(fenetre3, text="Option 2").pack()
    tk.Checkbutton(fenetre3, text="Option 3").pack()
    tk.Checkbutton(fenetre3, text="Option 4").pack()

    boutton_trois_valider = tk.Button(fenetre3, text="Suivant", command=lambda: ouvrir_quatrieme_fenetre(fenetre3))
    boutton_trois_valider.pack(pady=10)

    fenetre3.mainloop()
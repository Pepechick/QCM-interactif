from dictionnaires import DictioQCM

class questionnairetressimple:

    def __init__(self, QCM): 
        self.QCM = QCM

    def affiche_correction(self, question):
        """ fonction qui affiche la correction à la question
        --> renvoie un tuple avec (indice de la réponse , réponse correcte)"""
        
        for cle, valeur in self.QCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "*":
                        self.reponse = valeur[i][:-1]  # on enlève l’étoile
                        return (i+1, self.reponse)

        return None

    def affiche_gag(self, question):
        """ fonction qui affiche la réponse drôle
        --> renvoie un tuple avec (indice de la réponse , réponse spéciale drôle)"""
        
        for cle, valeur in self.QCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "!":
                        self.reponse = valeur[i][:-1]  # on enlève le point d'!
                        return (i+1, self.reponse)

        return None

    def affichageQCM(self, question):
        ''' permet d'afficher la question du QCM contenue dans le tableau QCM.
        les réponses sont ensuite proposées (l'étoile indiquant la bonne réponse est supprimée lors de l'affichage)'''
        
        print(f"Question : {question}")

        for cle, valeur in self.QCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "*":
                        print(i+1, " : ", valeur[i][:-1])
                    elif valeur[i][-1] == "!":
                        print(i+1, " : ", valeur[i][:-1])
                    else : 
                        print(i+1, " : ", valeur[i])

        self.r = int(input("Entrez le N° de votre réponse (1, 2, ou 3) : "))

        return self.r
        

    def score_reponse(self, rep, question):
        ''' calcul le score de la question n°i en fonction de la réponse
        --> renvoie 0 ou 1'''
        
        for cle, valeur in self.QCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "*":
                        self.rep_correcte = valeur[i][:-1]
    
        if self.rep_correcte == rep:
            self.score += 1
            return 1
        else:
            return 0

    def passageQCM(self):
        ''' fonction de passage de QCM. Pour chaque question :
        --> affiche la question puis les 3 propositions (fonction affichageQCM)
        --> récupère le numéro de la réponse du candidat dans un tableau
        --> affiche la correction  (fonction affiche_correction)
        --> comptabilise le score (fonction score_reponse)'''
        
        assert type(self.QCM) == list, "QCM doit être un tableau."
        pass

        print

r = questionnairetressimple(DictioQCM)
print(r.affichageQCM("drapeaux/Australie.png"))
print(r.affiche_correction("drapeaux/Australie.png"))
print(r.affiche_gag("drapeaux/Australie.png"))


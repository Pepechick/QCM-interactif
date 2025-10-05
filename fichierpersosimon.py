from dictionnaires import DictioQCM

def affiche_correction(question):
        """ fonction qui affiche la correction à la question i
        --> renvoie un tuple avec (indice de la réponse , réponse correcte)"""
        
        for cle, valeur in DictioQCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "*":
                        reponse = valeur[i][:-1]  # on enlève l’étoile
                        return (i+1, reponse)

        return None

def affiche_gag(question):
        """ fonction qui affiche la correction à la question i
        --> renvoie un tuple avec (indice de la réponse , réponse correcte)"""
        
        for cle, valeur in DictioQCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "!":
                        reponse = valeur[i][:-1]  # on enlève l’étoile
                        return (i+1, reponse)

        return None

print(affiche_gag("drapeaux/France.png"))
print(affiche_correction("drapeaux/France.png"))

def affichageQCM(question):
        ''' permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
        les réponses sont ensuite proposées (l'étoile indiquant la bonne réponse est supprimée lors de l'affichage)'''
        
        print(f"Question : {question}")

        for cle, valeur in DictioQCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "*":
                        print(i+1, " : ", valeur[i][:-1])
                    elif valeur[i][-1] == "!":
                        print(i+1, " : ", valeur[i][:-1])
                    else : 
                        print(i+1, " : ", valeur[i])

        r = int(input("Entrez le N° de votre réponse (1, 2, ou 3) : "))

        return r

def score_reponse(rep, question):
        ''' calcul le score de la question n°i en fonction de la réponse
        --> renvoie 0 ou 1'''
        
        for cle, valeur in DictioQCM.items():
            if cle == question:
                for i in range(len(valeur)):
                    if valeur[i][-1] == "*":
                        rep_correcte = valeur[i][:-1]
    
        if rep_correcte == rep:
            return 1
        else:
            return 0

print(score_reponse(affichageQCM("drapeaux/France.png"), "drapeaux/France.png"))


class questionnairetressimple:

    def __init__(self): 
        self.QCM = DictioQCM


    def affiche_correction(self, i):
        ''' fonction qui affiche la correction à la question i
        --> renvoie un tuple avec (indice de la réponse , réponse correcte)'''
        
        assert type(self.QCM) != 'list', "QCM doit être un tableau."
        assert i >= 0 and i <= 2, "i est compris entre 0 et 2."
        
        for k in range(1, 4):
            if self.QCM[k][i][0] == "*":
                reponse = self.QCM[k][i][1:]
                correction = (i, reponse)

        return correction


    def affichageQCM(self, i):
        ''' permet d'afficher la question n°i du QCM contenue dans le tableau QCM.
        les réponses sont ensuite proposées (l'étoile indiquant la bonne réponse est supprimée lors de l'affichage)'''
        
        assert type(self.QCM) != 'list', "QCM doit être un tableau."
        assert i >= 0 and i <= 2, "i est compris entre 0 et 2."
        
        print(self.QCM[0][i])
        
        for k in range(1, 4):
            if self.QCM[k][i][0] == "*":
                print(k, " : ", self.QCM[k][i][1:])
            else :
                print(k, " : ", self.QCM[k][i])
        
        r = int(input("Entrez le N° de votre réponse (1, 2, ou 3) : "))

        return r
        

    def score_reponse(self, rep, i):
        ''' calcul le score de la question n°i en fonction de la réponse
        --> renvoie 0 ou 1'''
        
        assert type(self.QCM) != 'list', "QCM doit être un tableau."
        assert rep > 0 and rep <= 3, "rep est compris entre 1 et 3."
        assert i >= 0 and i <= 2, "i est compris entre 0 et 2."

        rep_correcte = self.affiche_correction(i)[0]
    
        if rep_correcte == rep:
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
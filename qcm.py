class QCM:

    def __init__(self):
        "doc"






    def liste_rep(question, dico=self.QCM):
        assert question <= 10, "Attention, il n'y a que 10 question"
        i = 1
        for liste_reponses in dico.values():
            if i == question:
                r = liste_reponses
            i += 1
        return r

    def liste_quest(dico=self.QCM):
        i = 1
        q = []
        for quest in dico.keys():
            q.append(quest)
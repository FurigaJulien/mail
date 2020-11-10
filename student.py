
class Student:

    """Definition d'une classe pour chaque personne"""

    def __init__(self,nom,prenom,id,mail=""):
        self.nom=nom
        self.prenom=prenom
        self.id=id
        self.mail=mail


    def __repr__(self):
        return str(self.nom)+" "+str(self.mail)


class Mail():

    def __init__(self,mail):
        
        self.mail=mail

    def __repr__(self):
        return self.mail
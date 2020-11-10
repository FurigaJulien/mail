


class File:

    def __init__(self,fileName):
        self.fileName=fileName

    def readFile(self):
        with open(self.fileName, "r") as fichier:
	        return fichier.read()



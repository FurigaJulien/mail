from data import File
import mysql.connector
import re
from student import Student,Mail

class Bdd:

    def __init__(self):
        self.config = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'list_etudiants'
        }
        self.link = mysql.connector.connect(**self.config)
        self.cursor=self.link.cursor()
        


    def getStudent(self):
        studentList=[]
        get_query="SELECT etudiants.nom,etudiants.prenom,etudiants.id FROM etudiants "
        self.cursor.execute(get_query)
        liste=self.cursor.fetchall()

        for row in liste:

            nom=str(row[0])
            prenom=str(row[1])
            id=int(row[2])
            etudiant=Student(nom,prenom,id)
            studentList.append(etudiant)

        
        return studentList

    def saveMailFromFile(self,fileName):
        mailList= File(fileName).readFile().split("\n")[0:-1]
        returnList=[]
        for mail in mailList:
            
            #self.cursor.execute(query,(None,mail))
            #self.link.commit()
            studentMail=Mail(mail)
            print(studentMail)
            returnList.append(studentMail)
        
        return returnList



    def getStudentFromList(self,filename):

        liste=self.saveMailFromFile(filename)
        studentList=self.getStudent()
        finalList=[]
        for mail in liste:
            string=(mail.mail.split("@")[0].split("."))
            prenom=string[0]
            nom=string[1]
            for student in studentList:
                if prenom.lower()==student.prenom.lower() and nom.lower()==student.nom.replace(" ","-").replace("'","").replace("é","e").lower():
                    print(student.prenom)
                    student.mail=mail
                    finalList.append(student)
        print(finalList)
        self.saveMailWithUSer(finalList)
       
    def saveMailWithUSer(self,studentList):
        query="INSERT INTO `mail` VALUES (%s,%s,%s)"
        for student in studentList:
            self.cursor.execute(query,(None,student.mail.mail,student.id))
            self.link.commit()


    def closeBDD(self):
        self.cursor.close()
        self.link.close()
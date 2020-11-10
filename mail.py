
from base_de_donnee import Bdd
# Python program to create  
# a file explorer in Tkinter 
   
# import all components 
# from the tkinter library 
from tkinter import *
   
# import filedialog module 
from tkinter import filedialog 

# Function for opening the  
# file explorer window 
def browseFiles(): 
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 

def runImport():                                                       
    bdd=Bdd()
    bdd.getStudentFromList(filename)
    bdd.closeBDD()
    

def main():
    window = Tk() 
    window.title('File Explorer') 
    window.geometry("500x500") 
    window.config(background = "white") 
    label_file_explorer = Label(window,  
                                text = "File Explorer using Tkinter", 
                                width = 100, height = 4,  
                                fg = "blue")     
    button_explore = Button(window,  
                            text = "Browse Files", 
                            command = browseFiles)  
    button_exit = Button(window,  
                        text = "Exit", 
                        command = exit)
                        
    button_run = Button(window,text = "Lancer l'importation des mails", command = runImport)     
                      
    label_file_explorer.pack() 
    button_explore.pack() 
    button_run.pack(expand=YES)  
    button_exit.pack() 
    window.mainloop() 
    

main()
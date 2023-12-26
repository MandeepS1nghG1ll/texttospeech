#Importing necessary modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

#Creating the main window
root=Tk()
root.title("TEXT TO SPEECH")
root.geometry("900x450+100+100")
root.resizable(False,False)
root.configure(bg="medium Turquoise")

#Initializing the pyttsx3 engine
#pyttsx3 is a text to speech conversion library 
engine = pyttsx3.init()

#Defining a function to speak the text out loud
def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    # Defining a function to set the voice and speak the text
    def setvoice():
        if (gender == 'Male'):
            # Setting the voice to a male voice
            engine.setProperty('voice', voices[0].id)
            # Speaking the text using the pyttsx3 engine
            engine.say(text)
            engine.runAndWait()
        else:  
             # Setting the voice to a female voice
             engine.setProperty('voice', voices[1].id)
             # Speaking the text using the pyttsx3 engine
             engine.say(text)
             engine.runAndWait() 

    if (text):    
        if (speed == "Fast"):  # Setting the speaking rate to a fast speed
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):  # Setting the speaking rate to a normal speed
            engine.setProperty('rate', 150)     
            setvoice()
        else:    # Setting the speaking rate to a slow speed
            engine.setProperty('rate',60)
            setvoice()       


#Defining a function to save the spoken text as an mp3 file
def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    # Defining a function to set the voice and save the spoken text as an mp3 file
    def setvoice():
        if (gender == 'Male'):
            # Setting the voice to a male voice
            engine.setProperty('voice', voices[0].id)
            # Asking the user to select a directory to save the file in
            path=filedialog.askdirectory()
            os.chdir(path)
              # Saving the spoken text as an mp3 file
            engine.save_to_file(text,'textspeech.mp3')
            engine.runAndWait()
        else: 
             # Setting the voice to a female voice 
             engine.setProperty('voice', voices[1].id)
             path=filedialog.askdirectory()
             os.chdir(path)
             engine.save_to_file(text,'textspeech.mp3')
             engine.runAndWait() 


     # Checking if there is any text to SAVE
    if (text):  
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)     
            setvoice()
        else:   
            engine.setProperty('rate',60)
            setvoice()    


#top frame where the label(TEXT TO SPEECH) will be placed
Top_frame = Frame(root,bg="seashell2",width=900,height=100)
Top_frame.place(x=0,y=0)

#top label of the window
Label(Top_frame,text="TEXT TO SPEECH",font="funkydori 30",fg="midnight blue").place(x=280,y=25)

#Area where the text will be written, which will be converted to speech
text_area = Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

#labeling the gender and speed combobox
Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)

#combobox for selecting a male or female voice
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

#Combobox for selecting the speed of the speech
speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

#speak out button
btn=Button(root,text="Speak",compound=LEFT,width=9,height=1,bg="bisque",font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)

#download button
save=Button(root,text="Save",compound=LEFT,width=9,height=1,bg="aquamarine",font="arial 14 bold",command=download)
save.place(x=730,y=280)


root.mainloop()

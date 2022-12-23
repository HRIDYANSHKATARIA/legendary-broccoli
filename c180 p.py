from tkinter import *
import speech_recognition as sr 

root = Tk()

root.title("SPEECH TO TEXT")
root.geometry("400x400")

def r_audio():
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data = ''
        try:
            voice_data = speech_recognisor.recognize_google(audio,language='en-in')
        except sr.UnknownValueError:
            print("PLEASE REPEAT I DID NOT GET THAT")
    print(voice_data)
    
r_audio()

input_label = Entry()
input_label.place(relx=0.02,rely=0.2,anchor=W)

input_text = Text_Area()
input_text.place(relx=0.02,rely=0.5,anchor=W)


root.mainloop()
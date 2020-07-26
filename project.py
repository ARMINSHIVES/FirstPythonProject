import os
import playsound
from gtts import gTTS
import random
import string
from tkinter import *

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def speak(text):
	tts = gTTS(text=text, lang="en")
	name = randomString(7)
	filename = name +".mp3"
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)

tk = Tk()
btn = Button(tk, text = "click me", command=speak("hell0"))
btn.pack()
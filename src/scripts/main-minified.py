sounds=['nice-sound', 'police', 'python', 'omg']
from playsound import playsound
from time import sleep as PyWait
from random import randint as w, choice as h
def cls():
    from os import system
    system('clear')
PyWait(w(1, 5))
playsound(str('../audio/')+str(h(sounds))+'.mp3')

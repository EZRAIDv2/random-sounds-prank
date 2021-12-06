global sounds
sounds=['nice-sound', 'police', 'python', 'omg']
#'cute-bear'
from playsound import playsound
from time import sleep as PyWait
from random import randint as random_randint
from random import choice as random_choice
def cls():
    from os import system as sys, name as nm
    clearConsole = lambda: sys('cls' if nm in ('nt', 'dos') else 'clear')
    clearConsole()
cls()
PyWait(random_randint(1, 5))
playsound(str('../audio/')+str(random_choice(sounds))+'.mp3')

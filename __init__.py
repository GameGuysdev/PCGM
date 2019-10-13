name = "pcons"
import time
import pip
import subprocess
import sys
try:
        import keyboard
except ImportError as e:
        install("keyboard")
        time.sleep(0.5)
        import keyboard
        pass
try:
        from colorama import init
        from colorama import Fore, Back, Style
        init()
except ImportError as e:
        install("colorama")
        time.sleep(0.5)
        from colorama import init
        from colorama import Fore, Back, Style
        init()
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
class pcons:
    def __init__(self):
         print("welcome")
         self.sprite = self.sprite
    def sprite(self, spritename, x=0, y=0):
        m = ""
        m2 = ""
        for i in range(x):
            m += " "
        for i in range(y):
            m2 += "\n"
        words = ""
        file = open(".\\Sprites\\" + spritename + "\\" + spritename + ".sprite", "r")
        words = file.read()
        thi = ""
        for w in range(len(words)):
            if words[w] == "r":
                thi += Back.RED + " " + Back.BLACK
            if words[w] == "g":
                thi += Back.GREEN + " " + Back.BLACK
            if words[w] == "b":
                thi += Back.BLUE + " " + Back.BLACK
            if words[w]=="1":
                thi += Back.BLACK + "\n" + m
        return m + thi + m2
    def fill(self, color=Back.BLACK):
         print(color)
